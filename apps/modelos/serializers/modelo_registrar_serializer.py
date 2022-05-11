from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.modelos.models import Modelo
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios


class ModeloRegistrarSerializer(Serializer):
    mod_descripcion = serializers.CharField(required=True,
                                            error_messages={
                                                "required": "El nombre del modelo es requerido.",
                                                "blank": "El nombre del modelo no debe estar vacío.",
                                                "invalid": "El nombre del modelo debe ser válido.",
                                            })
    mod_estado = serializers.BooleanField(required=True,
                                          error_messages={
                                              "required": "El estado del modelo es requerido.",
                                              "blank": "El estado del modelo no debe estar vacío.",
                                              "invalid": "El estado del modelo debe ser válido.",
                                          })

    def validate_mod_descripcion(self, value):

        if len(str.strip(value)) >= 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    nombre_modelo = Modelo.objects.filter(mod_descripcion=value)
                    if not nombre_modelo.exists():
                        return value
                    else:
                        raise serializers.ValidationError('El modelo ya existe.')
                else:
                    raise serializers.ValidationError('El modelo debe contener caracteres alfabéticos.')

            else:
                raise serializers.ValidationError("El nombre del modelo no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre del modelo no debe tener menos de 4 caracteres.")

    def validate_mod_estado(self, value):
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado del modelo solo puede ser Verdadero o Falso")

    def create(self, data):
        descripcion = str(data.get('mod_descripcion')).upper()
        modelo_nuevo = Modelo(mod_descripcion=descripcion, mod_estado=True)
        modelo_nuevo.save()
