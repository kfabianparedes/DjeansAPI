from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from apps.roles.models import Rol
from apps.roles.serializers.rol_registrar_serializer import RolRegistroSerializer
from apps.roles.serializers.rol_serializer import RolSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission, \
    MetodoNoPermitidoPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import obtenerErrorSerializer
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class RolView(GenericViewSet):
    serializer_class = RolSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [EstaAutenticadoPermission]
        elif self.action == 'create':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'destroy':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        else:
            permission_classes = [MetodoNoPermitidoPermission]
        return [permission() for permission in permission_classes]

    def list(self, request):
        try:
            roles = Rol.objects.all()
            rol_serializer = RolSerializer(roles, many=True)
            return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, rol_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def create(self, request):
        try:
            crear_rol_serializer = RolRegistroSerializer(data=request.data)
            if crear_rol_serializer.is_valid():
                crear_rol_serializer.save()
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, success=True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                     message=obtenerErrorSerializer(crear_rol_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def destroy(self, request, pk=None):
        pass