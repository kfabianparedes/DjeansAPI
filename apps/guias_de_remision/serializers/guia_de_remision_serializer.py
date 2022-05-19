from rest_framework.serializers import ModelSerializer
from apps.guias_de_remision.models import GuiaDeRemision


class GuiaDeRemisionSerializer(ModelSerializer):
    class Meta:
        model = GuiaDeRemision
        fields = '__all__'
