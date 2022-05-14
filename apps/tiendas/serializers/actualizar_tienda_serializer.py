
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.serializers import Serializer
from apps.sucursales.models import Sucursal

from apps.tiendas.models import Tienda
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspaciosNumerosGuiones


class TiendaActualizarSerializer(Serializer):
    tie_id = serializers.IntegerField(required=True,
                                    error_messages={
                                        "required": "El ID de la Tienda es requerido.",
                                        "blank": "El ID de la Tienda no debe estar vacío.",
                                        "invalid": "El ID de la Tienda debe ser válido.",
                                    })
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
    # tie_suc_id = serializers.IntegerField(required=True,
    #                                         error_messages={"required": "El id de la Sucursal es requerido.",
    #                                                     "blank": "El id de la Sucursal no debe estar vacio",
    #                                                     "invalid": "El id de la Sucursal debe ser valido.",
    # 
    #                                                    })
    tie_suc_id=serializers.ReadOnlyField(source='sucursal.suc_id')
    # tie_suc_id=serializers.ReadOnlyField(source='SUCURSAL.SUC_ID')
    


    def validate_tie_nombre(self, value):
        if len(str.strip(value)) >= 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspaciosNumerosGuiones(value):
                    nombre_tienda = Tienda.objects.filter(tie_nombre=value).exclude(tie_id=self.instance.tie_id)
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

    def validate_tie_estado(self, value):
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado de la Tienda solo puede ser Verdadero o Falso")

    def update(self, instance, data):
        instance.tie_suc_id=Sucursal(data.get('tie_suc_id',instance.tie_suc_id))
        instance.tie_nombre = str(data.get('tie_nombre', instance.tie_nombre))
        instance.tie_estado = data.get('tie_estado', instance.tie_estado)
        return instance.save()
