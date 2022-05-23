from django.db import transaction
from rest_framework.viewsets import GenericViewSet

from django.db import DatabaseError
from rest_framework import status

from apps.compras import models
from apps.compras.models import Compra
from apps.compras.serializers.compras_serializer import CompraSerializer
from apps.compras.serializers.registrar_compra_serializer import CompraRegistrarSerializer
from apps.detalles_de_compra.serializers.registrar_detalle_de_compra_serializer import \
    DetalleDeCompraRegistrarSerializer
from apps.guias_de_remision.serializers.registrar_guia_remision_serializer import GuiaDeRemisionRegistrarSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class CompraView(GenericViewSet):

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
            queryset = models.Compra.objects.all().order_by('-comp_fecha_registro')
            productos_serializer = CompraSerializer(queryset, many=True)
            return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, productos_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def create(self, request):
        try:
            compra = CompraRegistrarSerializer(data=request.data.get('compra'))
            if compra.is_valid():
                with transaction.atomic():
                    compra.save()
                    last_purchase = Compra.objects.latest('comp_id')
                    purchase = CompraSerializer(last_purchase)

                    detalles = request.data.get('detalles')
                    for detail in detalles:
                        detail["compra"] = purchase.data.get('comp_id')
                        detalle = DetalleDeCompraRegistrarSerializer(data=detail)
                        if not detalle.is_valid():
                            transaction.set_rollback(rollback=True)
                            return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                                 message=obtenerErrorSerializer(detalle))
                        detalle.save()

                    guia_remision = request.data.get('guia_remision')
                    if guia_remision:
                        guia_remision["compra"] = purchase.data.get('comp_id')
                        guia = GuiaDeRemisionRegistrarSerializer(data=guia_remision)
                        if not guia.is_valid():
                            transaction.set_rollback(rollback=True)
                            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=obtenerErrorSerializer(guia))
                        guia.save()
                    return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, purchase.data, success=True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=obtenerErrorSerializer(compra))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
