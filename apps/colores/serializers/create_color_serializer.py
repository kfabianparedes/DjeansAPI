from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from apps.colores.models import Color
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios


class CreateColorSerializer(Serializer):
    col_descripcion = serializers.CharField(required=True,
                                            error_messages={
                                                "required": "El nombre del color es requerido.",
                                                "blank": "El nombre del color no debe estar vacío.",
                                                "invalid": "El nombre del color debe ser válido.",
                                            })
    col_estado = serializers.BooleanField(required=True,
                                          error_messages={
                                              "required": "El estado del color es requerido.",
                                              "blank": "El estado del color no debe estar vacío.",
                                              "invalid": "El estado del color debe ser válido.",
                                          })

    def validate_col_descripcion(self, value):

        if len(str.strip(
                value)) >= 3:  # validamos que el valor ingresado no sea menor a 3 pero antes le quitamos los espacios
            if len(value) <= 30:  # validamos que el valor ingresado no sea mayor a 30 sin quitarle los espacios
                if validarCaracteresAlfabeticoConEspacios(value):  # valiamos que el valor ingresado sea solo alfabético

                    nombre_color = Color.objects.filter(col_descripcion=value)

                    if not nombre_color.exists():
                        return value
                    else:
                        raise serializers.ValidationError("El color ya existe.")

                else:
                    raise serializers.ValidationError("El nombre del color solo debe contener caracteres alfabéticos.")
            else:
                raise serializers.ValidationError("El nombre del color no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre del color no debe tener menos de 3 caracteres.")

    def validate_col_estado(self, value):
        if type(value) == bool:
            if value:
                return value
            else:
                raise serializers.ValidationError("El nuevo color no se puede crear con estado Falso.")
        else:
            raise serializers.ValidationError("El estado del color solo puede ser Verdadero o Falso.")

    def create(self, value):
        descripcion = str(value['col_descripcion']).upper()
        categoria_nueva = Color(col_descripcion=descripcion, col_estado=True)
        categoria_nueva.save()
