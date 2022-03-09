from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from core.settings.base import BD_ERROR_MESSAGE, SUCCESS_MESSAGE
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.permissions.user_permission import SuperUsuarioPermission,EstaAutenticado
from core.assets.validations.obtener_error_serializer import *
from .serializers.actualizar_categoria_serializer import CategoriaActualizarSerializer, CategoriaActualizarParcialSerializer
from .serializers.registrar_categoria_serializer import CategoriaCrearSerializer
from .serializers.categoria_serializer import CategoriaSerializer
from . import models
from .models import Categoria


class CategoriaView(GenericViewSet):
    serializer_class = CategoriaSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [EstaAutenticado]
        elif self.action == 'retrieve':
            permission_classes = [EstaAutenticado, SuperUsuarioPermission]
        elif self.action == 'create':
            permission_classes = [EstaAutenticado, SuperUsuarioPermission]
        elif self.action == 'update':
            permission_classes = [EstaAutenticado, SuperUsuarioPermission]
        elif self.action == 'partial_update':
            permission_classes = [EstaAutenticado, SuperUsuarioPermission]
        else:
            permission_classes = [EstaAutenticado, SuperUsuarioPermission]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        try:
            cat_id_buscado = self.kwargs['pk']
            if validarEsNumerico(cat_id_buscado) and validarEsMayorQueCero(cat_id_buscado):
                categoria_obtenida = Categoria.objects.get(cat_id=cat_id_buscado)
                categoria_serializar = CategoriaSerializer(categoria_obtenida)
                return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE,categoria_serializar.data)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=mensaje)
        except Categoria.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="La categoría no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def list(self, request):
        try:
            if request.user.is_superuser:
                queryset = models.Categoria.objects.all()
                categorias_serializer = CategoriaSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, categorias_serializer.data)
            else:
                queryset = models.Categoria.objects.filter(cat_estado=True)
                categorias_serializer = CategoriaSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, categorias_serializer.data)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def create(self, request):
        try:
            crear_categoria_serializer = CategoriaCrearSerializer(data=request.data)
            if crear_categoria_serializer.is_valid():
                crear_categoria_serializer.create(request.data)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, crear_categoria_serializer.data)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=obtenerErrorSerializer(crear_categoria_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def update(self, request, pk=None):
        try:
            cat_id_buscado = self.kwargs['pk']
            if validarEsNumerico(cat_id_buscado) and validarEsMayorQueCero(cat_id_buscado):
                categoria_obtenida = Categoria.objects.get(cat_id=cat_id_buscado)
                if request.data.get('cat_id') == int(cat_id_buscado):
                    categoria_serializer = CategoriaActualizarSerializer(categoria_obtenida, data=request.data)
                    if categoria_serializer.is_valid():
                        categoria_serializer.update(categoria_obtenida, request.data)
                        return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, categoria_serializer.data)
                    else:
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=obtenerErrorSerializer(categoria_serializer))
                else:
                    mensaje = 'Los parámetros y el ID enviado deben coincidir.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje ='Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Categoria.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="La categoría no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def partial_update(self, request, pk=None):
        try:
            cat_id_buscado = self.kwargs['pk']
            if validarEsNumerico(cat_id_buscado) and validarEsMayorQueCero(cat_id_buscado):
                categoria_obtenida = Categoria.objects.get(cat_id=cat_id_buscado)
                categoria_serializer = CategoriaActualizarParcialSerializer(categoria_obtenida, data=request.data)
                if categoria_serializer.is_valid():
                    categoria_serializer.update(categoria_obtenida, request.data)
                    return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, categoria_serializer.data)
                else:
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=obtenerErrorSerializer(categoria_serializer))
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Categoria.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="La categoría no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def destroy(self, request, pk=None):
        try:
            cat_id_buscado = self.kwargs['pk']
            if validarEsNumerico(cat_id_buscado) and validarEsMayorQueCero(cat_id_buscado):
                categoria_obtenida = Categoria.objects.filter(cat_id=cat_id_buscado).update(cat_estado=False)
                print(categoria_obtenida)
                if categoria_obtenida==1:
                    return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE)
                else:
                    mensaje = 'La categoría no existe.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=mensaje)
            else:
                mensaje ='Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Categoria.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="La categoría no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

