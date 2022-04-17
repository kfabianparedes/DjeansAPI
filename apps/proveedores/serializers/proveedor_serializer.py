from rest_framework.serializers import ModelSerializer
from apps.proveedores.models import Proveedor


class ProveedorSerializer(ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
