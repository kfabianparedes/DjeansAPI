from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from apps.productos import models
from apps.productos.serializers.producto_serializer import ProductoSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission, \
    MetodoNoPermitidoPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class ProductByProviderView(GenericViewSet):

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [EstaAutenticadoPermission]
        else:
            permission_classes = [EstaAutenticadoPermission, MetodoNoPermitidoPermission]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        try:
            print(self.kwargs['pk'])
            provider = self.kwargs['pk']
            queryset = models.Producto.objects.filter(proveedor=provider, prod_estado=True)
            productos_serializer = ProductoSerializer(queryset, many=True)
            return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, productos_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)