from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from core.assets.permissions.user_permission import SuperUsuarioPermission, EstaAutenticadoPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import BD_ERROR_MESSAGE, SUCCESS_MESSAGE
from apps.inventarios import models
from apps.inventarios.models import Inventario
from apps.tiendas.models import Tienda
from apps.inventarios.serializers.inventario_serializer import InventarioSerializer
# Create your views here.

class InventarioView(GenericViewSet):

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [EstaAutenticadoPermission]
        # elif self.action == 'retrieve':
        #     permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        # elif self.action == 'create':
        #     permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        # elif self.action == 'update':
        #     permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        # elif self.action == 'partial_update':
        #     permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        # else:
        #     permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        try:
            # if request.user.is_superuser:
            #     queryset = models.Inventario.objects.all()
            #     Inventario_serializer = InventarioSerializer(queryset, many=True)
            #     return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, Inventario_serializer.data, True)
            # else:
            #     queryset = models.Inventario.objects.all()
            #     Inventario_serializer = InventarioSerializer(queryset, many=True)
            #     return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, Inventario_serializer.data, True)

            id_tienda = self.kwargs['pk']
            if validarEsNumerico(id_tienda) and validarEsMayorQueCero(id_tienda):
                tienda_enviada = Tienda.objects.filter(tie_id=id_tienda)
                if tienda_enviada.exists():
                    queryset = models.Inventario.objects.filter(tienda=id_tienda)
                    inventario_serializer = InventarioSerializer(queryset, many=True)
                    return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, inventario_serializer.data, True)
                else:
                    mensaje = 'La tienda ingresada no existe.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deber ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)

        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)