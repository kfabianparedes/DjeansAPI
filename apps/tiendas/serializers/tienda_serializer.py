from rest_framework.serializers import ModelSerializer
from apps.tiendas.models import Tienda


class TiendaSerializer(ModelSerializer):
    class Meta:
        model = Tienda
        fields = '__all__'
