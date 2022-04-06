from rest_framework.serializers import ModelSerializer
from apps.proveedores.models import PROVEEDORES

class ProveedorSerializer(ModelSerializer):
    class Meta:
        model=PROVEEDORES
        fields='__all__'