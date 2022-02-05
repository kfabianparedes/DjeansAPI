from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class UsuarioManager(BaseUserManager):
    def _create_user(self, username, email, nombres,apellidos, password, is_staff, is_superuser, **extra_fields):
        usuario = self.model(
            username = username,
            email = email,
            nombres = nombres,
            apellidos = apellidos,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        usuario.set_password(password = password)
        usuario.save(using=self.db)
        return usuario

    def create_user(self, username, email, nombres,apellidos, password=None, **extra_fields):
        return self._create_user(username, email, nombres,apellidos, password, False, False, **extra_fields)

    def create_superuser(self, username, email, nombres,apellidos, password=None, **extra_fields):
        return self._create_user(username, email, nombres,apellidos, password, True, True, **extra_fields)
