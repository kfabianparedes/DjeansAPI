from dataclasses import field
from rest_framework.serializers import ModelSerializer
from apps.compras.models import Compra

class ReporteCompraSerializer(ModelSerializer):
    class Meta:
        model:Compra
        fields='__all__'