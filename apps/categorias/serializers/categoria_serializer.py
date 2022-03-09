from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.categorias.models import Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

