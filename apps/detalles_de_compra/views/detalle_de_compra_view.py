from django.db import transaction
from rest_framework.viewsets import GenericViewSet

from django.db import DatabaseError
from rest_framework import status

from apps.compras import models
from apps.compras.serializers.compras_serializer import CompraSerializer
from apps.compras.serializers.registrar_compra_serializer import CompraRegistrarSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class DetalleDeCompraView(GenericViewSet):
    pass
    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [EstaAutenticadoPermission]
    #     elif self.action == 'create':
    #         permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
    #     elif self.action == 'update':
    #         permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
    #     elif self.action == 'destroy':
    #         permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
    #     else:
    #         permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
    #     return [permission() for permission in permission_classes]

    # def list(self, request):
    #     try:
    #         pass
    #     except DatabaseError:
    #         return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
    #
    # def create(self, request):
    #     try:
    #         pass
    #     except DatabaseError:
    #         return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
