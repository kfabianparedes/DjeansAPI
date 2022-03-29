from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.sucursales.models import SUCURSALES
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios

class SucursalCrearSerializer(Serializer):
    SUC_NOMBRE=serializers.CharField(required=True,
                                    error_messages={"required":"El nombre de la Sucursal es requerido.",
                                                    "blank":"El nombre de la Sucursal no debe estar vacio",
                                                    "invalid": "El nombre de la Sucursal debe ser valido.",
                                                    })
    SUC_DIRECCION=serializers.CharField(required=True,
                                        error_messages={"required":"La direccion de la Sucursal es requerido.",
                                                        "blank":"La direccion de la Sucursal no debe estar vacio",
                                                        "invalid": "La direccion de la Sucursal debe ser valido.",
                                                        })
    SUC_ESTADO=serializers.BooleanField(required=True,
                                        error_messages={"required":"El estado de la Sucursal es requerido.",
                                                        "blank":"El estado de la Sucursal no debe estar vacio",
                                                        "invalid": "El estado de la Sucursal debe ser valido.",
                                                        })

    def validate_SUC_NOMBRE(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    nombre_sucursal = SUCURSALES.objects.filter(SUC_NOMBRE=value)
                    if not nombre_sucursal.exists():
                        return value
                    else:
                        raise serializers.ValidationError('La Sucursal ya existe.')
                else:
                    raise serializers.ValidationError('La Sucursal debe contener caracteres alfabéticos.')

            else:
                raise serializers.ValidationError("El nombre de la Sucursal no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre de la Sucursal no debe tener menos de 4 caracteres.")

    def validate_SUC_DIRECCION(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    direccion_sucursal = SUCURSALES.objects.filter(SUC_DIRECCION=value)
                else:
                    raise serializers.ValidationError('La Direccion de la Sucursal debe contener caracteres alfabéticos.')

            else:
                raise serializers.ValidationError("La Direccion de la Sucursal no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("La Direccion de la Sucursal no debe tener menos de 4 caracteres.")

    def validate_SUC_ESTADO(self, value):
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado de la Sucursal solo puede ser Verdadero o Falso")

    def create(self, data):
        nombre = str(data['SUC_NOMBRE']).upper()
        direccion=str(data['SUC_DIRECCION']).upper()
        categoria_nueva = SUCURSALES(SUC_NOMBRE=nombre, SUC_DIRECCION=direccion,SUC_ESTADO=True)
        categoria_nueva.save()