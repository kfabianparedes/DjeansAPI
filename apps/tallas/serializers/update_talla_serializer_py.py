from rest_framework.serializers import Serializer
from rest_framework import serializers
from apps.tallas.models import Talla
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios


class UpdateTallaSerializer(Serializer):
    tal_id = serializers.IntegerField(required=True,
                                      error_messages={
                                          "required": "El ID de la talla es requerido.",
                                          "blank": "El ID de la talla no puede estar vacío.",
                                          "invalid": "El ID de la talla debe ser válido."
                                      })
    tal_descripcion = serializers.CharField(required=True,
                                            error_messages={
                                                "required": "El nombre de la talla es requerido.",
                                                "blank": "El nombre de la talla no puede estar vacío.",
                                                "invalid": "El nombre de la talla debe ser válido."
                                            })
    tal_estado = serializers.BooleanField(required=True,
                                          error_messages={
                                              "required": "El estado de la talla es requerido.",
                                              "blank": "El estado de la talla no puede estar vacío.",
                                              "invalid": "El estado de la talla debe ser válido."
                                          })

    def validate_tal_descripcion(self, value):

        if len(str.strip(value)) > 0:  # validamos que el valor ingresado no sea menor a 3 pero antes le quitamos los espacios
            if len(value) <= 30:  # validamos que el valor ingresado no sea mayor a 30 sin quitarle los espacios
                if validarCaracteresAlfabeticoConEspacios(value):  # valiamos que el valor ingresado sea solo alfabético

                    nombre_talla = Talla.objects.filter(tal_descripcion=value).exclude(
                        tal_id = self.instance.tal_id
                    )

                    if not nombre_talla.exists():
                        return value
                    else:
                        raise serializers.ValidationError("El color ya existe.")

                else:
                    raise serializers.ValidationError("El nombre de la talla solo debe contener caracteres alfabéticos.")
            else:
                raise serializers.ValidationError("El nombre de la talla no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre de la talla no debe tener menos de 3 caracteres.")

    def validate_tal_estado(self, value):
        if type(value) == bool:

            return value

        else:
            raise serializers.ValidationError("El estado de la talla solo puede ser Verdadero o Falso.")

    def update(self, instance, data):
        instance.tal_descripcion = str(data.get('tal_descripcion',instance.tal_descripcion)).upper()
        instance.cat_estado = data.get('tal_estado',instance.tal_estado)
        return instance.save()