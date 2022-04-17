from operator import truediv
from rest_framework import serializers
from rest_framework.serializers import Serializer
from apps.sucursales.models import Sucursal

from apps.tiendas.models import Tienda
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios


class TiendaCrearSerializer(Serializer):
    tie_nombre = serializers.CharField(required=True,
                                       error_messages={"required": "El nombre de la Tienda es requerido.",
                                                       "blank": "El nombre de la Tienda no debe estar vacio",
                                                       "invalid": "El nombre de la Tienda debe ser valido.",
                                                       })
    tie_estado = serializers.BooleanField(required=True,
                                          error_messages={"required": "El estado de la Tienda es requerido.",
                                                          "blank": "El estado de la Tienda no debe estar vacio",
                                                          "invalid": "El estado de la Tienda debe ser valido.",
                                                          })
    tie_suc_id = serializers.IntegerField(required=True,
                                          error_messages={"required": "El id de la Sucursal es requerido.",
                                                          "blank": "El id de la Sucursal no debe estar vacio",
                                                          "invalid": "El id de la Sucursal debe ser valido.",
                                                          })

    def validate_tie_nombre(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    nombre_tienda = Tienda.objects.filter(tie_nombre=value)
                    if not nombre_tienda.exists():
                        return value
                    else:
                        raise serializers.ValidationError('La Tienda ya existe.')
                else:
                    raise serializers.ValidationError('La Tienda debe contener caracteres alfabéticos.')

            else:
                raise serializers.ValidationError("El nombre de la Tienda no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre de la Tienda no debe tener menos de 4 caracteres.")

    def validate_tie_suc_id(self, value):
        if value > 0:
            print("ATTRS ", value)
            verifica_id = Sucursal.objects.filter(SUC_ID=value).exists()
            print("ExisteSucursal ", verifica_id)
            if not verifica_id:
                raise serializers.ValidationError("No existe tal Sucursal")
        else:
            raise serializers.ValidationError("El Id de sucursal no es valido")

    def validate_tie_estado(self, value):
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado de la Tienda solo puede ser Verdadero o Falso")

    def create(self, data):

        nombre = str(data['tie_nombre']).upper()
        instanciamiento = Sucursal()
        instanciamiento.suc_id = str(data["tie_suc_id"])

        tienda_nueva = Tienda(tie_nombre=nombre, tie_estado=True, tie_suc_id=instanciamiento)
        print("TIENDA NUEVA: ", tienda_nueva)
        tienda_nueva.save()
