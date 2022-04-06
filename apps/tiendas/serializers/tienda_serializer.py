from rest_framework.serializers import ModelSerializer
from apps.tiendas.models import TIENDAS

class TiendaSerializer(ModelSerializer):
    
    class Meta:
        model=TIENDAS
        fields='__all__'