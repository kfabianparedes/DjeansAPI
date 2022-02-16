from rest_framework import serializers
from apps.usuarios.clases import TipoDocumento


class TipoDocumentoSerializar(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'
