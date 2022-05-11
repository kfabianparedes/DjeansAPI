from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.roles.models import Rol
from apps.usuarios.models import Usuario
from core.assets.validations.obtener_error_serializer import validarEsNumerico, validarCaracteresAlfabeticoConEspacios


class UsuarioRegistrarSerializer(Serializer):
    username = serializers.CharField(required=True,
                                     error_messages={
                                         'required': 'El usuario es requerido.',
                                         'blank': 'El usuario no debe estar vacío.',
                                         'invalid': 'El usuario debe ser válido.',

                                     })
    password = serializers.CharField(required=True,
                                     error_messages={
                                         'required': 'La contraseña es requerida.',
                                         'null': 'La contraseña no debe estar vacío.',
                                         'invalid': 'La contraseña debe ser válida.',
                                     })
    rol = serializers.IntegerField(required=True,
                                   error_messages={
                                       'required': 'El rol es requerido',
                                       'null': 'El rol no debe ser estar vacío.',
                                       'invalid': 'El rol debe ser un número entero.',
                                   })

    def validate_username(self, value):
        if len(str.strip(value)) >= 5:
            if len(str.strip(value)) <= 50:
                if validarCaracteresAlfabeticoConEspacios(value):
                    username = Usuario.objects.filter(username=value)
                    if not username.exists():
                        return value
                    else:
                        raise serializers.ValidationError('El nombre de usuario ya existe.')
                else:
                    raise serializers.ValidationError("El nombre de usuario solo acepta caracteres alfabéticos.")
            else:
                raise serializers.ValidationError("El nombre de usuario debe tener máximo 50 caracteres.")
        else:
            raise serializers.ValidationError("El nombre de usuario debe tener mínimo 5 caracteres.")

    def validate_password(self, value):
        if len(str.strip(value)) >= 8:
            if len(str.strip(value)) <= 50:
                return value
            else:
                raise serializers.ValidationError("La contraseña debe tener máximo 50 caracteres.")
        else:
            raise serializers.ValidationError("La contraseña debe tener mínimo 8 caracteres.")

    def validate_rol(self, value):
        if validarEsNumerico(value):
            rol = Rol.objects.filter(rol_id=value)
            if rol.exists():
                return value
            else:
                raise serializers.ValidationError("El rol no está registrado.")
        else:
            raise serializers.ValidationError("El rol debe ser un número entero.")

    def save(self, **kwargs):
        username = str(self.data.get('username')).upper()
        password = self.data.get('password')
        rol = self.data.get('rol')
        role = Rol.objects.filter(rol_id=rol, rol_tipo='SUPERUSUARIO')
        if role.exists():
            return Usuario.objects.create_superuser(
                username=username,
                password=password,
                rol=rol,
            )
        else:
            return Usuario.objects.create_user(
                username=username,
                password=password,
                rol=rol
            )

