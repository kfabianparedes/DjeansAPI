from rest_framework.serializers import ModelSerializer
from apps.usuarios.models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("id", "username", "is_staff", "is_employee", "is_superuser", "is_active")
