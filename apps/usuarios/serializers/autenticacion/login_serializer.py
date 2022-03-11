from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.usuarios.models import Usuario


class LoginSerializer(Serializer):
    username = serializers.CharField(required=True,
                                     error_messages={
                                         "required": "El nombre de usuario es requerido.",
                                         "blank": "El nombre de usuario no debe estar vacío.",
                                         "invalid": "El nombre de usuario debe ser válido.",
                                     })
    password = serializers.CharField(required=True,
                                     error_messages={
                                         "required": "La contraseña es requerida.",
                                         "blank": "La contraseña no debe estar vacía.",
                                         "invalid": "La contraseña debe ser válida.",
                                     })

    def validate_username(self, value):
        nombre_categoria = Usuario.objects.filter(username=value)
        if nombre_categoria.exists():
            return value
        else:
            raise serializers.ValidationError('El nombre de usuario no le pertenece a una cuenta.')

    def validate_password(self, value):
        if len(value) > 5:
            return value
        else:
            raise serializers.ValidationError('La contraseña tiene menos de 8 caracteres.')
