from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from apps.usuarios.estado_civil_model import EstadoCivil
from apps.usuarios.serializers.estado_civil.estado_civil_serializer import EstadoCivilSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, MetodoSegurosPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class EstadoCivilView(GenericViewSet):
    serializer_class = EstadoCivilSerializer
    permission_classes = [MetodoSegurosPermission, EstaAutenticadoPermission]
    queryset = EstadoCivil.objects.all()

    def list(self, request):
        try:
            estado_civil_serializer = self.serializer_class(self.queryset, many=True)
            return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, estado_civil_serializer.data)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
