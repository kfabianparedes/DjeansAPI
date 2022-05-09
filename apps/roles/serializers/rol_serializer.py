from rest_framework.serializers import ModelSerializer
from apps.roles.models import Rol


class RolSerializer(ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
