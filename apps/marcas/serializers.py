from rest_framework import serializers

from apps.marcas.models import Marca


class MarcaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
