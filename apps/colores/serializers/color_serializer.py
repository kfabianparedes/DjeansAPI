from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apps.colores.models import Color


class ColorSerializer(ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'