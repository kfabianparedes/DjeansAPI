from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from apps.productos import models
from apps.productos.serializers.producto_serializer import ProductoSerializer
from apps.productos.serializers.registrar_producto_serializer import ProductoRegistrarSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import obtenerErrorSerializer
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class ProductoView(GenericViewSet):

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [EstaAutenticadoPermission]
        elif self.action == 'create':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'update':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'destroy':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        else:
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        return [permission() for permission in permission_classes]

    def list(self, request):
        try:
            if request.user.is_superuser:
                queryset = models.Producto.objects.all()
                productos_serializer = ProductoSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, productos_serializer.data, True)
            else:
                queryset = models.Producto.objects.filter(prod_estado=True)
                productos_serializer = ProductoSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, productos_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def create(self, request):
        try:
            registrar_producto_serializer = ProductoRegistrarSerializer(data=request.data)
            if registrar_producto_serializer.is_valid():
                registrar_producto_serializer.create(request.data)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, registrar_producto_serializer.data, True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                     message=obtenerErrorSerializer(registrar_producto_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
