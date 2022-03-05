from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UsuarioManager
from .clases import TipoDocumento, EstadoCivil
from django.utils import timezone


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Nombre de usuario", max_length=255, unique=True)
    is_active = models.BooleanField("Activo/Inactivo", default=True)
    is_staff = models.BooleanField("Administrador", default=False, )
    is_employee = models.BooleanField("Empleado", default=True)
    is_superuser = models.BooleanField("Super Usuario", default=False)
    register_date = models.DateField("Fecha creación", default=timezone.now)
    objects = UsuarioManager()

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['is_employee', 'is_superuser']

    def __str__(self):
        return f'{self.username}'


class InformacionPersonal(models.Model):
    INFO_PER_ID = models.BigAutoField(verbose_name='Inf. Personal Nº', primary_key=True)
    INFO_PER_NOMBRES = models.CharField(verbose_name='Nombres', max_length=50, blank=True, null=True)
    INFO_PER_APELLIDOS = models.CharField(verbose_name='Apellidos', max_length=50, blank=True, null=True)
    INFO_PER_EMAIL = models.EmailField(verbose_name='Email', max_length=50, unique=True, blank=True, null=True)
    INFO_PER_GENERO = models.CharField(verbose_name='Género', max_length=1, blank=False, null=False, default='F')
    INFO_PER_FECHA_NACIMIENTO = models.DateField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
    INFO_PER_DIRECCION1 = models.TextField(verbose_name='Dirección 1', max_length=100, blank=True, null=True)
    INFO_PER_DIRECCION2 = models.TextField(verbose_name='Dirección 2', max_length=100, blank=True, null=True)
    INFO_PER_CELULAR1 = models.CharField(verbose_name='Nro. Celular 1', max_length=9, blank=True, null=True)
    INFO_PER_CELULAR2 = models.CharField(verbose_name='Nro. Celular 2', max_length=9, blank=True, null=True)
    USUARIO = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True, blank=True,
                                   null=True, verbose_name='Usuario')
    ESTADO_CIVIL_ID = models.OneToOneField(EstadoCivil, on_delete=models.CASCADE, unique=True, blank=True, null=True,
                                           verbose_name='Estado Civil')
    TIPO_DOC_PER_ID = models.OneToOneField(TipoDocumento, on_delete=models.CASCADE, unique=True, blank=True, null=True,
                                           verbose_name='Tipo de documento')
    INFO_PER_DOCUMENTO_IDENTIDAD = models.CharField(verbose_name='Nro. Documento', max_length=11, blank=True, null=True)

    class Meta:
        db_table = 'informacion_personal'
        verbose_name = 'Información Personal'
        verbose_name_plural = 'Informaciones personales'

    def __str__(self):
        return f'{self.INFO_PER_NOMBRES} {self.INFO_PER_APELLIDOS}'
