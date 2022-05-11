from rest_framework.serializers import ModelSerializer

from apps.marcas.models import Marca


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
