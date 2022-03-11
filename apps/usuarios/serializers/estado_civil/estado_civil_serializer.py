from rest_framework.serializers import ModelSerializer
from apps.usuarios.estado_civil_model import EstadoCivil


class EstadoCivilSerializer(ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = '__all__'
