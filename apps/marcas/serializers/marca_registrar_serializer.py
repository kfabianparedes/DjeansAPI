from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.marcas.models import Marca
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios


class MarcaRegistrarSerializer(Serializer):
    mar_descripcion = serializers.CharField(required=True,
                                            error_messages={
                                                "required": "El nombre de la marca es requerido.",
                                                "blank": "El nombre de la marca no debe estar vacío.",
                                                "invalid": "El nombre de la marca debe ser válido.",
                                            })
    mar_estado = serializers.BooleanField(required=True,
                                          error_messages={
                                              "required": "El estado de la marca es requerido.",
                                              "blank": "El estado de la marca no debe estar vacío.",
                                              "invalid": "El estado de la marca debe ser válido.",
                                          })

    def validate_mar_descripcion(self, value):

        if len(str.strip(value)) >= 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    nombre_Marca = Marca.objects.filter(mar_descripcion=value)
                    if not nombre_Marca.exists():
                        return value
                    else:
                        raise serializers.ValidationError('La marca ya está registrada.')
                else:
                    raise serializers.ValidationError('La marca debe contener caracteres alfabéticos.')

            else:
                raise serializers.ValidationError("El nombre de la marca no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre de la marca no debe tener menos de 4 caracteres.")

    def validate_mar_estado(self, value):
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado de la marca solo puede ser Verdadero o Falso")

    def save(self, **kwargs):
        descripcion = str(self.data.get('mar_descripcion')).upper()
        nueva_marca = Marca(mar_descripcion=descripcion, mar_estado=True)
        nueva_marca.save()
