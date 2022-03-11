from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.usuarios.models import Usuario
from core.assets.validations.obtener_error_serializer import validarEsNumerico


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
                                       'invalid': 'El rol debe ser válido.',
                                   })

    def validate_username(self, value):
        if len(str.strip(value)) >= 5:
            if len(str.strip(value)) <= 50:
                if str(value).isalpha():
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
        if validarEsNumerico(str(value)) and (0 < value < 4):
            return value
        raise serializers.ValidationError("El rol debe ser un número entero entre 1 y 3.")

    def create(self, data):
        username = data['username']
        password = data['password']
        rol = data['rol']

        if rol == 1:
            return Usuario.objects.create_superuser(
                username=username,
                password=password)
        elif rol == 2:
            return Usuario.objects.create_admin(
                username=username,
                password=password)
        elif rol == 3:
            return Usuario.objects.create_employee(
                username=username,
                password=password)
