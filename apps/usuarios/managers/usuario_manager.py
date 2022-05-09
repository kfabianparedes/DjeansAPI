from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class UsuarioManager(BaseUserManager):

    def create_superuser(self, username, password, rol, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('register_date', timezone.now())
        nuevo_usuario = self.model(username=username, rol=rol, **extra_fields)
        nuevo_usuario.set_password(password)
        nuevo_usuario.save()

    def create_user(self, username, password, rol, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('register_date', timezone.now())
        nuevo_usuario = self.model(username=username, rol=rol, **extra_fields)
        nuevo_usuario.set_password(password)
        nuevo_usuario.save()

