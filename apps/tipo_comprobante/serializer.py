from rest_framework.serializers import ModelSerializer

from apps.tipo_comprobante.models import TipoComprobante


class TipoComprobanteSerializer(ModelSerializer):
    class Meta:
        model = TipoComprobante
        fields = '__all__'
