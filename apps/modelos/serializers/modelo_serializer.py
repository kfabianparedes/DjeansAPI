from rest_framework.serializers import ModelSerializer

from apps.modelos.models import Modelo


class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'
