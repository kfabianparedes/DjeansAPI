from rest_framework import serializers
from rest_framework.serializers import Serializer
from apps.colores.models import Color


class UpdateColorSerializer(Serializer):

    col_id = serializers.IntegerField(required=True,
                                            error_messages={
                                                "required": "El ID del color es requerido",
                                                "blank": "El ID del color no debe estar vacío",
                                                "invalid": "El ID del color debe ser válido",
                                            })
    col_descripcion = serializers.CharField(required=True,
                                            error_messages={
                                                "required": "El nombre del color es requerido",
                                                "blank": "El nombre del color no debe estar vacío",
                                                "invalid": "El nombre del color debe ser válido",
                                            })
    col_estado = serializers.BooleanField(required=True,
                                          error_messages={
                                              "required": "El estado del color es requerido",
                                              "blank": "El estado del color no debe estar vacío",
                                              "invalid": "El estado del color debe ser válido",
                                          })
    def validate_col_descripcion(self, value):

        if len(str.strip(value)) >= 3: # validamos que el valor ingresado no sea menor a 3 pero antes le quitamos los espacios
            if len(value) <= 30: # validamos que el valor ingresado no sea mayor a 30 sin quitarle los espacios
                if str(value).isalpha(): # valiamos que el valor ingresado sea solo alfabético

                    nombre_color = Color.objects.filter(col_descripcion=value).exclude(
                        col_id = self.instance.col_id)

                    if not nombre_color.exists():
                        return value
                    else:
                        raise serializers.ValidationError("El color ya existe.")

                else:
                    raise serializers.ValidationError("El nombre solo debe contener caracteres alfabéticos.")
            else:
                raise serializers.ValidationError("El nombre del color no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre del color no debe tener menos de 3 caracteres.")

    def validate_col_estado(self, value):
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado del color solo puede ser Verdadero o Falso.")

    def update(self, instance, data):
        instance.col_descripcion = str(data.get('col_descripcion',instance.col_descripcion)).upper()
        instance.col_estado = data.get('col_estado',instance.col_estado)
        return instance.save()