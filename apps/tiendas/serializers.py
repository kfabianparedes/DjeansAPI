from rest_framework import serializers

from apps.tiendas.models import TIENDAS
class tiendasSerializers(serializers.ModelSerializer):
    class Meta:
        model=TIENDAS
        fields=['TIE_ID','TIE_NOMBRE','TIE_ESTADO','TIE_SUC_ID']
        
