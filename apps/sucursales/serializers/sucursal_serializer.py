from rest_framework.serializers import ModelSerializer
from apps.sucursales.models import Sucursal


class SucursalSerializer(ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'
