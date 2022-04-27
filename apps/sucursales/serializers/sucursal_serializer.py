from rest_framework.serializers import ModelSerializer
from apps.sucursales.models import Sucursal
from apps.tiendas.serializers.tienda_serializer import TiendaSerializer


class SucursalSerializer(ModelSerializer):
    # tiendas=TiendaSerializer(many=True)
    class Meta:
        model = Sucursal
        # fields = ('suc_id','suc_nombre','suc_direccion','suc_estado','tiendas')
        fields = ('suc_id','suc_nombre','suc_direccion','suc_estado')
