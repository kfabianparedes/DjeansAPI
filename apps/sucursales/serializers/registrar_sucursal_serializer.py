from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.sucursales.models import Sucursal
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspaciosNumerosGuiones
from core.assets.validations.obtener_error_serializer import validarCaracteresAlnumconEspaciosGuionesNumeralesPuntos


class SucursalCrearSerializer(Serializer):
    suc_nombre = serializers.CharField(required=True,
                                       error_messages={"required": "El nombre de la Sucursal es requerido.",
                                                       "blank": "El nombre de la Sucursal no debe estar vacio",
                                                       "invalid": "El nombre de la Sucursal debe ser valido.",
                                                       })
    suc_direccion = serializers.CharField(required=True,
                                          error_messages={"required": "La direccion de la Sucursal es requerido.",
                                                          "blank": "La direccion de la Sucursal no debe estar vacio",
                                                          "invalid": "La direccion de la Sucursal debe ser valido.",
                                                          })
    suc_estado = serializers.BooleanField(required=True,
                                          error_messages={"required": "El estado de la Sucursal es requerido.",
                                                          "blank": "El estado de la Sucursal no debe estar vacio",
                                                          "invalid": "El estado de la Sucursal debe ser valido.",
                                                          })

    def validate_suc_nombre(self, value):
        if len(str.strip(value)) >= 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspaciosNumerosGuiones(value):
                    nombre_sucursal = Sucursal.objects.filter(suc_nombre=value)
                    if not nombre_sucursal.exists():
                        return value
                    else:
                        raise serializers.ValidationError('La sucursal ya existe.')
                else:
                    raise serializers.ValidationError('El nombre de la sucursal es inválido.')

            else:
                raise serializers.ValidationError("El nombre de la sucursal no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre de la sucursal no debe tener menos de 4 caracteres.")

    def validate_suc_direccion(self, value):
        if len(str.strip(value)) >= 4:
            if len(value) <= 30:
                if validarCaracteresAlnumconEspaciosGuionesNumeralesPuntos(value):
                    return value
                else:
                    raise serializers.ValidationError('La dirección de la sucursal debe contener caracteres alfabéticos.')

            else:
                raise serializers.ValidationError("La dirección de la sucursal es inválida.")
        else:
            raise serializers.ValidationError("La dirección de la sucursal no debe tener menos de 4 caracteres.")

    def validate_suc_estado(self, value):
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado de la sucursal solo puede ser Verdadero o Falso")

    def create(self, data):
        nombre = str(data['suc_nombre']).upper()
        direccion = str(data['suc_direccion']).upper()
        categoria_nueva = Sucursal(suc_nombre=nombre, suc_direccion=direccion, suc_estado=True)
        categoria_nueva.save()
