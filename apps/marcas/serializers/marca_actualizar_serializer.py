from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.marcas.models import Marca
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios


class MarcaActualizarSerializer(Serializer):
    mar_id = serializers.IntegerField(required=True,
                                      error_messages={
                                          "required": "El ID dLa marca es requerido.",
                                          "blank": "El ID dLa marca no debe estar vacío.",
                                          "invalid": "El ID dLa marca debe ser válido.",
                                      })
    mar_descripcion = serializers.CharField(required=True,
                                            error_messages={
                                                "required": "El nombre dLa marca es requerido.",
                                                "blank": "El nombre dLa marca no debe estar vacío.",
                                                "invalid": "El nombre dLa marca debe ser válido.",
                                            })
    mar_estado = serializers.BooleanField(required=True,
                                          error_messages={
                                              "required": "El estado dLa marca es requerido.",
                                              "blank": "El estado dLa marca no debe estar vacío.",
                                              "invalid": "El estado dLa marca debe ser válido.",
                                          })

    def validate_mar_descripcion(self, value):

        if len(str.strip(value)) >= 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    nombre_marca = Marca.objects.filter(mar_descripcion=value).exclude(
                        mar_id=self.instance.mar_id)
                    if not nombre_marca.exists():
                        return value
                    else:
                        raise serializers.ValidationError('La marca ya existe.')
                else:
                    raise serializers.ValidationError('La marca debe contener caracteres alfabéticos.')

            else:
                raise serializers.ValidationError("El nombre de la marca no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre de la marca no debe tener menos de 4 caracteres.")

    def validate_mar_estado(self, value):
        if value is True or value is False:
            return value
        else:
            raise serializers.ValidationError("El estado de la marca solo puede ser Verdadero o Falso")

    def update(self, instance, data):
        instance.mar_descripcion = str(data.get('mar_descripcion', instance.mar_descripcion)).upper()
        instance.mar_estado = data.get('mar_estado', instance.mar_estado)
        return instance.save()
