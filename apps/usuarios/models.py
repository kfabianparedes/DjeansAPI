from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# class UsuarioManager(BaseUserManager):
#     def _create_user(self, username ,password, is_staff, is_superuser, **extra_fields):
#         usuario = self.model(
#             username = username,
#             is_staff = is_staff,
#             is_superuser = is_superuser,
#             **extra_fields
#         )
#         usuario.set_password(password)
#         usuario.save(using=self.db)
#         return usuario

#     def create_user(self, username, password=None, **extra_fields):
#         return self._create_user(username,password, False, False, **extra_fields)

#     def create_superuser(self, username, password=None, **extra_fields):
#         return self._create_user(username, password, True, True, **extra_fields)
class UsuarioManager(BaseUserManager):
    def create_user(self, username,email, password, **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        extra_fields.setdefault('is_employee', True)
        extra_fields.setdefault('is_active', True)
        user = self.model(username=username, email= email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_employee', True)
        #if extra_fields.get('is_staff') is not True:
            #raise ValueError(_('Superuser must have is_staff=True.'))
        #if extra_fields.get('is_superuser') is not True:
            #raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username,email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField("Email", max_length=254, unique= True)
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
    REQUIRED_FIELDS = ['email, is_employee']

    def __str__(self):
        return f'{self.username}'