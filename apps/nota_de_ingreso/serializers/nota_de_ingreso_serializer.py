from rest_framework.serializers import ModelSerializer
from apps.nota_de_ingreso.models import NotaDeIngreso


class NotaDeIngresoSerializer(ModelSerializer):
    class Meta:
        model = NotaDeIngreso
        fields = '__all__'
