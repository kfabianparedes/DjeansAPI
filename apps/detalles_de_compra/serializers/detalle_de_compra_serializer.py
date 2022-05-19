from rest_framework.serializers import ModelSerializer
from apps.detalles_de_compra.models import DetalleDeCompra


class DetalleDeCompraSerializer(ModelSerializer):
    class Meta:
        model = DetalleDeCompra
        fields = '__all__'
