from django.conf import settings
from django.db import models

from apps.usuarios.estado_civil_model import EstadoCivil
from apps.usuarios.models import Usuario
from apps.usuarios.tipo_de_documento_model import TipoDeDocumento


class InformacionPersonal(models.Model):
    info_per_id = models.BigAutoField(verbose_name='Inf. Personal Nº', primary_key=True)
    info_per_nombres = models.CharField(verbose_name='Nombres', max_length=50, blank=True, null=True)
    info_per_apellidos = models.CharField(verbose_name='Apellidos', max_length=50, blank=True, null=True)
    info_per_email = models.EmailField(verbose_name='Email', max_length=50, unique=True, blank=True, null=True)
    info_per_genero = models.CharField(verbose_name='Género', max_length=1, blank=False, null=False, default='F')
    info_per_fecha_nac = models.DateField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
    info_per_direc_1 = models.TextField(verbose_name='Dirección 1', max_length=100, blank=True, null=True)
    info_per_direc_2 = models.TextField(verbose_name='Dirección 2', max_length=100, blank=True, null=True)
    info_per_cel_1 = models.CharField(verbose_name='Nro. Celular 1', max_length=9, blank=True, null=True)
    info_per_cel_2 = models.CharField(verbose_name='Nro. Celular 2', max_length=9, blank=True, null=True)
    usuario = models.IntegerField(verbose_name='Usuario', unique=True, blank=False, null=False)
    estado_civil = models.IntegerField(verbose_name='Estado Civil', unique=True, blank=False, null=False)
    tipo_documento = models.IntegerField(verbose_name='Tipo de documento', unique=True, blank=False, null=False)
    info_per_nro_doc = models.CharField(verbose_name='Nro. Documento', max_length=11, blank=True, null=True)

    class Meta:
        db_table = 'informacion_personal'
        verbose_name = 'Información Personal'
        verbose_name_plural = 'Informaciones personales'

    def __str__(self):
        return f'{self.info_per_nombres} {self.info_per_apellidos}'
