from rest_framework.serializers import ModelSerializer
from apps.detalles_de_ingreso.models import DetalleDeIngreso


class DetalleDeIngresoSerializer(ModelSerializer):
    class Meta:
        model = DetalleDeIngreso
        fields = '__all__'
