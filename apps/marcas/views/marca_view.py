from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from apps.marcas.models import Marca
from apps.marcas.serializers.marca_actualizar_serializer import MarcaActualizarSerializer
from apps.marcas.serializers.marca_registrar_serializer import MarcaRegistrarSerializer
from apps.marcas.serializers.marca_serializer import MarcaSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission, \
    MetodoNoPermitidoPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import obtenerErrorSerializer, validarEsNumerico, \
    validarEsMayorQueCero
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class MarcaView(GenericViewSet):
    serializer_class = MarcaSerializer

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [EstaAutenticadoPermission]
        elif self.action == 'destroy':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'create':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'update':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        else:
            permission_classes = [MetodoNoPermitidoPermission]
        return [permission() for permission in permission_classes]

    def list(self, request):
        try:
            if request.user.is_superuser:
                queryset = Marca.objects.all().order_by('-mar_estado', 'mar_descripcion')
                marca_serializer = MarcaSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, marca_serializer.data, True)
            else:
                queryset = Marca.objects.filter(mar_estado=True).order_by('mar_descripcion')
                marca_serializer = MarcaSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, marca_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def create(self, request):
        try:
            crear_marca_serializer = MarcaRegistrarSerializer(data=request.data)
            if crear_marca_serializer.is_valid():
                crear_marca_serializer.save()
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, success=True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                     message=obtenerErrorSerializer(crear_marca_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
        
    def update(self, request, pk=None):
        try:
            id_marca_buscada = self.kwargs['pk']
            if validarEsNumerico(id_marca_buscada) and validarEsMayorQueCero(id_marca_buscada):
                marca_obtenido = Marca.objects.get(mar_id=id_marca_buscada)
                if request.data.get('mar_id') == int(id_marca_buscada):
                    marca_serializer = MarcaActualizarSerializer(marca_obtenido, data=request.data)
                    if marca_serializer.is_valid():
                        marca_serializer.update(marca_obtenido, request.data)
                        return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, success=True)
                    else:
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                             message=obtenerErrorSerializer(marca_serializer))
                else:
                    mensaje = 'Los parámetros y el ID enviado deben coincidir.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Marca.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="La marca no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def destroy(self, request, pk=None):
        try:
            id_marca_buscada = self.kwargs['pk']
            if validarEsNumerico(id_marca_buscada) and validarEsMayorQueCero(id_marca_buscada):
                marca_obtenido = Marca.objects.get(mar_id=id_marca_buscada)
                marca_actualizada = MarcaSerializer(marca_obtenido)
                filas_modificadas = Marca.objects.filter(mar_id=id_marca_buscada).update(
                    mar_estado=not marca_actualizada.data.get('mar_estado'))
                if filas_modificadas == 1:
                    return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, success=True)
                else:
                    mensaje = 'La marca no existe o no se ha podido desactivar/activar.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Marca.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="La marca no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
