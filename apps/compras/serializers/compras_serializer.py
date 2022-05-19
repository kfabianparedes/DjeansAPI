from rest_framework.serializers import ModelSerializer
from apps.compras.models import Compra


class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'
