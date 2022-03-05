from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class UsuarioManager(BaseUserManager):

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_employee', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('register_date', timezone.now())
        nuevo_usuario = self.model(username=username, **extra_fields)
        nuevo_usuario.set_password(password)
        nuevo_usuario.save()
        return nuevo_usuario

    def create_admin(self, username, password, **extra_fields):
        extra_fields.setdefault('is_employee', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('register_date', timezone.now())
        nuevo_usuario = self.model(username=username, **extra_fields)
        nuevo_usuario.set_password(password)
        nuevo_usuario.save()
        return nuevo_usuario

    def create_employee(self, username, password, **extra_fields):
        extra_fields.setdefault('is_employee', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('register_date', timezone.now())
        nuevo_usuario = self.model(username=username, **extra_fields)
        nuevo_usuario.set_password(password)
        nuevo_usuario.save()
        return nuevo_usuario

    # def create_employee(self, username, password, **extra_fields):
    #     if not username:
    #         raise ValueError('El username es requerido')
    #     if not password:
    #         raise ValueError('La contraseña es requerida')
    #
    #     extra_fields.setdefault('is_employee', True)
    #     extra_fields.setdefault('is_active', True)
    #
    #     nuevo_usuario = self.model(username=username, **extra_fields)
    #     nuevo_usuario.set_password(password)
    #     nuevo_usuario.save()
    #     return nuevo_usuario
    #
    # def create_admin(self, username, password, **extra_fields):
    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('El rol de aministrador debe estar activado. (is_staff = True) ')
    #     return self.create_employee(username, password, **extra_fields)
    #
    # def create_superuser(self, username, password, **extra_fields):
    #
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('El rol de superusuario debe estar activado. (is_superuser = True) ')
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #
    #     return self.create_admin(username, password, **extra_fields)
