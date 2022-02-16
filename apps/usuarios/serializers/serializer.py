from rest_framework import serializers
from apps.usuarios.models import Usuario


class UsuarioTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'id',)


class UserSerializer(serializers.ModelSerializer):
    pass

