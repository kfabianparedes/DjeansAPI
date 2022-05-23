from django.db import DatabaseError
from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet

from apps.tipo_comprobante import models
from apps.tipo_comprobante.serializer import TipoComprobanteSerializer
from core.assets.permissions.user_permission import *
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class TipoComprobanteView(GenericViewSet):

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [EstaAutenticadoPermission]
        else:
            permission_classes = [MetodoNoPermitidoPermission]
        return [permission() for permission in permission_classes]

    def list(self, request):
        try:
            queryset = models.TipoComprobante.objects.all()
            talla_serializer = TipoComprobanteSerializer(queryset, many=True)
            return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, talla_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
