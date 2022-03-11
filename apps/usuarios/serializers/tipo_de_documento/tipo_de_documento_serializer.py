from rest_framework.serializers import ModelSerializer

from apps.usuarios.tipo_de_documento_model import TipoDeDocumento


class TipoDeDocumentoSerializer(ModelSerializer):
    class Meta:
        model = TipoDeDocumento
        fields = '__all__'
