from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.roles.models import Rol
from apps.usuarios.managers.usuario_manager import UsuarioManager
from django.utils import timezone


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Nombre de usuario", max_length=255, unique=True)
    is_active = models.BooleanField("Activo/Inactivo", default=True)
    is_superuser = models.BooleanField("Super Usuario", default=False)
    register_date = models.DateField("Fecha creación", default=timezone.now)
    rol = models.IntegerField("Rol", blank=False)
    objects = UsuarioManager()

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rol', 'is_superuser']

    def __str__(self):
        return f'{self.username}'
