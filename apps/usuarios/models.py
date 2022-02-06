from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UsuarioManager
from .clases import TipoDocumento, EstadoCivil
class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_employee = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    register_date = models.DateField("Fecha creación", auto_now=False, auto_now_add=True)
    objects = UsuarioManager()

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['is_employee','is_superuser']

    def __str__(self):
        return f'{self.username}'

class InformacionPersonal(models.Model):
    INFO_PER_ID = models.BigAutoField(verbose_name='Inf. Personal Nº',primary_key=True)
    INFO_PER_NOMBRES = models.CharField(max_length=50, blank= True, null= True)
    INFO_PER_APELLIDOS = models.CharField(max_length=50, blank= True, null= True)
    INFO_PER_EMAIL = models.EmailField(max_length=50, unique= True, blank= True, null= True)
    INFO_PER_GENERO = models.CharField(max_length=1, blank= False, null= False, default='F')
    INFO_PER_FECHA_NACIMIENTO = models.DateField(blank=True, null= True)
    INFO_PER_DIRECCION1 = models.TextField(max_length=100, blank= True , null= True)
    INFO_PER_DIRECCION2 = models.TextField(max_length=100, blank= True , null= True)
    INFO_PER_CELULAR1 = models.CharField(max_length=9, blank= True , null= True)
    INFO_PER_CELULAR2 = models.CharField(max_length=9, blank= True , null= True)
    INFO_PER_DOCUMENTO_IDENTIDAD = models.CharField(max_length=11, blank= True , null= True)
    USU_ID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE , unique= True, blank= True, null= True)
    ESTADO_CIVIL_ID = models.OneToOneField(EstadoCivil, on_delete= models.CASCADE , unique= True, blank= True, null= True)
    TIPO_DOC_PER_ID = models.OneToOneField(TipoDocumento, on_delete= models.CASCADE , unique= True, blank= True, null= True)

    class Meta:
        db_table = 'informacion_personal'
        verbose_name = 'Información Personal'
        verbose_name_plural = 'Informaciones personales'

    def __str__(self):
        return f'{self.INFO_PER_NOMBRES} {self.INFO_PER_APELLIDOS}'


