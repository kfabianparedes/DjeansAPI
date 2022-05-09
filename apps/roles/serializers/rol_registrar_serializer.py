from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.roles.models import Rol
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios


class RolRegistroSerializer(Serializer):
    rol_tipo = serializers.CharField(required=True,
                                     error_messages={
                                         "required": "El nombre del rol es requerido.",
                                         "blank": "El nombre del rol no debe estar vacío.",
                                         "invalid": "El nombre del rol debe ser válido.",
                                     })

    def validate_rol_tipo(self, value):
        if len(str.strip(value)) >= 4:
            if len(value) <= 20:
                if validarCaracteresAlfabeticoConEspacios(value):
                    nombre_rol = Rol.objects.filter(rol_tipo=value)
                    if not nombre_rol.exists():
                        return value
                    else:
                        raise serializers.ValidationError('El rol ya existe.')
                else:
                    raise serializers.ValidationError('El rol debe contener caracteres alfabéticos.')

            else:
                raise serializers.ValidationError("El tipo del rol no debe tener más de 20 caracteres.")
        else:
            raise serializers.ValidationError("El tipo del rol no debe tener menos de 4 caracteres.")

    def save(self, **kwargs):
        tipo = str(self.data.get('rol_tipo')).upper()
        rol_nuevo = Rol(rol_tipo=tipo)
        rol_nuevo.save()
