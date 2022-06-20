from django.db import transaction
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets

from django.db import DatabaseError
from rest_framework import status
from apps.detalles_de_compra.models import DetalleDeCompra
from apps.detalles_de_compra.serializers.detalle_de_compra_serializer import DetalleDeCompraSerializer
from apps.detalles_de_compra import models
from apps.compras.serializers.compras_serializer import CompraSerializer
from apps.compras.serializers.registrar_compra_serializer import CompraRegistrarSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class DetalleDeCompraView(GenericViewSet):

    def retrieve(self, request, pk=None):
        try:
            id_compra = self.kwargs['pk']
            if validarEsNumerico(id_compra) and validarEsMayorQueCero(id_compra):
                compra_enviada = DetalleDeCompra.objects.filter(compra=id_compra)
                if compra_enviada.exists():
                    queryset = models.DetalleDeCompra.objects.filter(compra=id_compra)
                    detalleCompra_serializer = DetalleDeCompraSerializer(queryset, many=True)
                    return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, detalleCompra_serializer.data, True)
                else:
                    mensaje = 'La compra ingresada no existe.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deber ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)

        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def list(self, request):
        try:
            # id_compra = 2
            # print(id_compra)
            queryset = modelsDetalleCompra.DetalleDeCompra.objects.all()
            detalle_compra_serializer = DetalleDeCompraSerializer(queryset, many=True)
            return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, detalle_compra_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)
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
