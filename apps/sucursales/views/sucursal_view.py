from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from core.assets.permissions.user_permission import SuperUsuarioPermission, EstaAutenticadoPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import BD_ERROR_MESSAGE, SUCCESS_MESSAGE
from apps.sucursales import models
from apps.sucursales.models import SUCURSALES, Sucursal
from apps.sucursales.serializers.actualizar_sucursal_serializer import SucursalActualizarSerializer
# from apps.categorias.serializers.actualizar_parcialmente_categoria_serializer import CategoriaActualizarParcialSerializer
from apps.sucursales.serializers.sucursal_serializer import SucursalSerializer
from apps.sucursales.serializers.registrar_sucursal_serializer import SucursalCrearSerializer

class SucursalView(GenericViewSet):
    def list(self, request):
        try:
            if request.user.is_superuser:
                queryset = models.SUCURSALES.objects.all()
                sucursales_serializer = SucursalSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, sucursales_serializer.data, True)
            else:
                queryset = models.Categoria.objects.filter(SUC_ESTADO=True)
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
                sucursal_obtenida = SUCURSALES.objects.get(SUC_ID=suc_id_buscado)
                if request.data.get('cat_id') == int(suc_id_buscado):
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
        except SUCURSALES.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="La Sucursal no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
