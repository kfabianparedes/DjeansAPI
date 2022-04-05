from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from apps.modelos import models
from apps.modelos.models import Modelo
from apps.modelos.serializers.actualizar_model_serializer import ModeloActualizarSerializer
from apps.modelos.serializers.modelo_serializer import ModeloSerializer
from apps.modelos.serializers.registrar_modelo_serializer import ModeloCrearSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission, \
    MetodoNoPermitidoPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import obtenerErrorSerializer, validarEsMayorQueCero, \
    validarEsNumerico
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class ModeloView(GenericViewSet):
    serializer_class = ModeloSerializer

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
            permission_classes = [MetodoNoPermitidoPermission]
        return [permission() for permission in permission_classes]

    def list(self, request):
        try:
            if request.user.is_superuser:
                queryset = models.Modelo.objects.all().order_by('-mod_estado', 'mod_descripcion')
                modelo_serializer = ModeloSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, modelo_serializer.data, True)
            else:
                queryset = models.Modelo.objects.filter(mod_estado=True).order_by('mod_descripcion')
                modelo_serializer = ModeloSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, modelo_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def create(self, request):
        try:
            crear_modelo_serializer = ModeloCrearSerializer(data=request.data)
            if crear_modelo_serializer.is_valid():
                crear_modelo_serializer.create(request.data)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, crear_modelo_serializer.data, True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                     message=obtenerErrorSerializer(crear_modelo_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
        
    def update(self, request, pk=None):
        try:
            mod_id_buscado = self.kwargs['pk']
            if validarEsNumerico(mod_id_buscado) and validarEsMayorQueCero(mod_id_buscado):
                modelo_obtenido = Modelo.objects.get(mod_id=mod_id_buscado)
                if request.data.get('mod_id') == int(mod_id_buscado):
                    modelo_serializer = ModeloActualizarSerializer(modelo_obtenido, data=request.data)
                    if modelo_serializer.is_valid():
                        modelo_serializer.update(modelo_obtenido, request.data)
                        return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, modelo_serializer.data, True)
                    else:
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                             message=obtenerErrorSerializer(modelo_serializer))
                else:
                    mensaje = 'Los parámetros y el ID enviado deben coincidir.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Modelo.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="El modelo no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def destroy(self, request, pk=None):
        try:
            mod_id_buscado = self.kwargs['pk']
            if validarEsNumerico(mod_id_buscado) and validarEsMayorQueCero(mod_id_buscado):
                modelo_obtenido = Modelo.objects.get(mod_id=mod_id_buscado)
                modelo_actualizado = ModeloSerializer(modelo_obtenido)
                filas_modificadas = Modelo.objects.filter(mod_id=mod_id_buscado).update(
                    mod_estado=not modelo_actualizado.data.get('mod_estado'))
                if filas_modificadas == 1:
                    return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, success=True)
                else:
                    mensaje = 'El modelo no existe o no se ha podido desactivar/activar.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Modelo.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="El modelo no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
