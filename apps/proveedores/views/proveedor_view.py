from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from core.assets.permissions.user_permission import SuperUsuarioPermission, EstaAutenticadoPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import BD_ERROR_MESSAGE, SUCCESS_MESSAGE
from apps.proveedores import models

from apps.proveedores.models import Proveedor
from apps.proveedores.serializers.actualizar_proveedor_serializer import ProveedorActualizarSerializer
from apps.proveedores.serializers.proveedor_serializer import ProveedorSerializer
from apps.proveedores.serializers.registrar_proveedor_serializer import ProveedorCrearSerializer


class ProveedorView(GenericViewSet):
    serializer_class = ProveedorSerializer

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
                queryset = models.Proveedor.objects.all().order_by('pro_estado','pro_nombre')
                proveedores_serializers = ProveedorSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, proveedores_serializers.data, True)
            else:
                queryset = models.Proveedor.objects.filter(pro_estado=True).order_by('pro_estado','pro_nombre')
                proveedores_serializers = ProveedorSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, proveedores_serializers.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def create(self, request):
        try:
            crear_proveedores_serializer = ProveedorCrearSerializer(data=request.data)
            if crear_proveedores_serializer.is_valid():
                crear_proveedores_serializer.create(request.data)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, crear_proveedores_serializer.data, True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                     message=obtenerErrorSerializer(crear_proveedores_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def update(self, request, pk=None):
        try:
            pro_id_buscado = self.kwargs['pk']
            if validarEsNumerico(pro_id_buscado) and validarEsMayorQueCero(pro_id_buscado):
                proveedor_obtenido = Proveedor.objects.get(pro_id=pro_id_buscado)
                if request.data.get('pro_id') == int(pro_id_buscado):
                    proveedor_serializer = ProveedorActualizarSerializer(proveedor_obtenido, data=request.data)
                    if proveedor_serializer.is_valid():
                        proveedor_serializer.update(proveedor_obtenido, request.data)
                        return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, proveedor_serializer.data, True)
                    else:
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                             message=obtenerErrorSerializer(proveedor_serializer))
                else:
                    mensaje = 'Los parámetros y el ID enviado deben coincidir.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Proveedor.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="El proveedor no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def destroy(self,request, pk=None):
        try:
            pro_id_obtenido = self.kwargs['pk']
            if validarEsNumerico(pro_id_obtenido) and validarEsMayorQueCero(pro_id_obtenido):
                proveedor_obtenido = Proveedor.objects.get(pro_id=pro_id_obtenido)
                proveedor_actuaizado = ProveedorSerializer(proveedor_obtenido)
                filas_modificadas = Proveedor.objects.filter(pro_id=pro_id_obtenido).update(
                    pro_estado=not proveedor_actuaizado.data.get('pro_estado')
                )
                if filas_modificadas == 1:
                    return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, success=True)
                else:
                    mensaje = 'El proveedor no existe o no se ha podido desactivar/activar.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)

        except Proveedor.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="El proveedor no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
