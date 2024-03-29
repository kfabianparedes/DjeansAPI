from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from core.assets.permissions.user_permission import SuperUsuarioPermission, EstaAutenticadoPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import BD_ERROR_MESSAGE, SUCCESS_MESSAGE
from apps.sucursales import models
from apps.sucursales.models import Sucursal
from apps.sucursales.serializers.actualizar_sucursal_serializer import SucursalActualizarSerializer
from apps.sucursales.serializers.sucursal_serializer import SucursalSerializer
from apps.sucursales.serializers.registrar_sucursal_serializer import SucursalCrearSerializer


class SucursalView(GenericViewSet):
    serializer_class = SucursalSerializer

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
                queryset = models.Sucursal.objects.all()
                sucursales_serializer = SucursalSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, sucursales_serializer.data, True)
            else:
                queryset = models.Sucursal.objects.filter(suc_estado=True)
                sucursales_serializer = SucursalSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, sucursales_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def create(self, request):
        try:
            crear_sucursal_serializer = SucursalCrearSerializer(data=request.data)
            if crear_sucursal_serializer.is_valid():
                crear_sucursal_serializer.create(request.data)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, crear_sucursal_serializer.data, True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                    message=obtenerErrorSerializer(crear_sucursal_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def update(self, request, pk=None):
        try:
            suc_id_buscado = self.kwargs['pk']
            if validarEsNumerico(suc_id_buscado) and validarEsMayorQueCero(suc_id_buscado):
                sucursal_obtenida = Sucursal.objects.get(suc_id=suc_id_buscado)
                if request.data.get('suc_id') == int(suc_id_buscado):
                    sucursal_serializer = SucursalActualizarSerializer(sucursal_obtenida, data=request.data)
                    if sucursal_serializer.is_valid():
                        sucursal_serializer.update(sucursal_obtenida, request.data)
                        return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, sucursal_serializer.data, True)
                    else:
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                            message=obtenerErrorSerializer(sucursal_serializer))
                else:
                    mensaje = 'Los parámetros y el ID enviado deben coincidir.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Sucursal.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="La sucursal no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def destroy (self, request, pk=None):
        try:
            suc_id_buscado = self.kwargs['pk']
            if validarEsNumerico(suc_id_buscado) and validarEsMayorQueCero(suc_id_buscado):
                sucursal_obtenida = Sucursal.objects.get(suc_id=suc_id_buscado)
                sucursal_actualizado = SucursalSerializer(sucursal_obtenida)
                filas_modificadas = Sucursal.objects.filter(suc_id=suc_id_buscado).update(
                    suc_estado=not sucursal_actualizado.data.get('suc_estado'))
                if filas_modificadas == 1:
                    return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, success=True)
                else:
                    mensaje = 'La Sucursal no existe o no se ha podido desactivar/activar.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Sucursal.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="La Sucursal no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
