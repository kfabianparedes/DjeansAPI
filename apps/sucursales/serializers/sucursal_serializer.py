from dataclasses import fields
from pyexpat import model
from django.urls import clear_script_prefix
from matplotlib.pyplot import cla
from rest_framework.serializers import ModelSerializer
from apps.sucursales.models import SUCURSALES

class SucursalSerializer(ModelSerializer):
    class Meta:
        model=SUCURSALES
        fields='__all__'