from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from core.assets.permissions.user_permission import SuperUsuarioPermission, EstaAutenticadoPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import BD_ERROR_MESSAGE, SUCCESS_MESSAGE
from apps.tiendas import models

from apps.tiendas.models import Tienda
from apps.tiendas.serializers.actualizar_tienda_serializer import TiendaActualizarSerializer
from apps.tiendas.serializers.tienda_serializer import TiendaSerializer
from apps.tiendas.serializers.registrar_tienda_serializer import TiendaCrearSerializer


class TiendaView(GenericViewSet):
    serializer_class = TiendaSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [EstaAutenticadoPermission]
        elif self.action == 'create':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'update':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        else:
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        return [permission() for permission in permission_classes]

    def list(self, request):
        try:
            if request.user.is_superuser:
                queryset = models.Tienda.objects.all()
                tiendas_serializers = TiendaSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, tiendas_serializers.data, True)
            else:
                queryset = models.Tienda.objects.filter(tie_estado=True)
                tiendas_serializers = TiendaSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, tiendas_serializers.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def create(self, request):
        try:
            crear_tiendas_serializer = TiendaCrearSerializer(data=request.data)
            if crear_tiendas_serializer.is_valid():
                crear_tiendas_serializer.create(request.data)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, crear_tiendas_serializer.data, True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                    message=obtenerErrorSerializer(crear_tiendas_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def update(self, request, pk=None):
        try:
            tie_id_buscado = self.kwargs['pk']
            if validarEsNumerico(tie_id_buscado) and validarEsMayorQueCero(tie_id_buscado):
                tienda_obtenida = Tienda.objects.get(tie_id=tie_id_buscado)
                if request.data.get('tie_id') == int(tie_id_buscado):
                    tienda_serializer = TiendaActualizarSerializer(tienda_obtenida, data=request.data)
                    if tienda_serializer.is_valid():
                        tienda_serializer.update(tienda_obtenida, request.data)
                        return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, tienda_serializer.data, True)
                    else:
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                            message=obtenerErrorSerializer(tienda_serializer))
                else:
                    mensaje = 'Los parámetros y el ID enviado deben coincidir.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Tienda.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="La Tienda no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
