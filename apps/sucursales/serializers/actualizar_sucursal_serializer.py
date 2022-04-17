from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.sucursales.models import Sucursal
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios


class SucursalActualizarSerializer(Serializer):
    suc_id = serializers.IntegerField(required=True,
                                      error_messages={
                                          "required": "El ID de la sucursal es requerido.",
                                          "blank": "El ID de la sucursal no debe estar vacío.",
                                          "invalid": "El ID de la sucursal debe ser válido.",
                                      })
    suc_nombre = serializers.CharField(required=True,
                                       error_messages={"required": "El nombre de la sucursal es requerido.",
                                                       "blank": "El nombre de la sucursal no debe estar vacio",
                                                       "invalid": "El nombre de la sucursal debe ser valido.",
                                                       })
    suc_direccion = serializers.CharField(required=True,
                                          error_messages={"required": "La direccion de la sucursal es requerido.",
                                                          "blank": "La direccion de la sucursal no debe estar vacio",
                                                          "invalid": "La direccion de la sucursal debe ser valido.",
                                                          })
    suc_estado = serializers.BooleanField(required=True,
                                          error_messages={"required": "El estado de la sucursal es requerido.",
                                                          "blank": "El estado de la sucursal no debe estar vacio",
                                                          "invalid": "El estado de la sucursal debe ser valido.",
                                                          })

    def validate_suc_nombre(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    nombre_sucursal = sucursal.objects.filter(suc_nombre=value)
                    if not nombre_sucursal.exists():
                        return value
                    else:
                        raise serializers.ValidationError('La sucursal ya existe.')
                else:
                    raise serializers.ValidationError('La sucursal debe contener caracteres alfabéticos.')

            else:
                raise serializers.ValidationError("El nombre de la sucursal no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre de la sucursal no debe tener menos de 4 caracteres.")

    def validate_suc_direccion(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    direccion_sucursal = sucursal.objects.filter(suc_direccion=value)
                else:
                    raise serializers.ValidationError(
                        'La dirección de la sucursal debe contener caracteres alfabéticos.')

            else:
                raise serializers.ValidationError("La dirección de la sucursal no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("La dirección de la sucursal no debe tener menos de 4 caracteres.")

    def validate_suc_estado(self, value):
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado de la sucursal solo puede ser Verdadero o Falso")

    def update(self, instance, data):
        instance.suc_nombre = str(data.get('suc_nombre', instance.suc_nombre)).upper()
        instance.suc_direccion = str(data.get('suc_direccion', instance.suc_direccion)).upper()
        instance.suc_estado = data.get('suc_estado', instance.suc_estado)
        return instance.save()
