from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.usuarios.models import Usuario
from core.assets.validations.obtener_error_serializer import validarEsNumerico


class LogoutSerializer(Serializer):
    username = serializers.CharField(required=True,
                                     error_messages={
                                         "required": "El nombre de usuario es requerido.",
                                         "blank": "El nombre de usuario no debe estar vacío.",
                                         "invalid": "El nombre de usuario debe ser válido.",
                                     })
    id = serializers.IntegerField(required=True,
                                  error_messages={
                                      "required": "El id de usuario es requerido.",
                                      "blank": "El id de usuario no debe estar vacío.",
                                      "invalid": "El id de usuario debe ser válido.",
                                  })

    def validate_id(self, value):
        if validarEsNumerico(str(value)):
            return value
        raise serializers.ValidationError("El id de usuario debe ser numérico.")

    def validate_username(self, value):
        nombre_categoria = Usuario.objects.filter(username=value)
        if nombre_categoria.exists():
            return value
        else:
            raise serializers.ValidationError('El nombre de usuario no le pertenece a una cuenta.')
