
from rest_framework.serializers import ModelSerializer
from apps.sucursales.models import SUCURSALES

class SucursalSerializer(ModelSerializer):
    class Meta:
        model=SUCURSALES
        fields='__all__'