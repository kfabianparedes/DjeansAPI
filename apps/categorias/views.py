from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from core.assets.permissions.user_permission import IsAuthenticated, SuperUsuarioPermission
from core.assets.validations.obtener_error_serializer import obtenerErrorSerializer
from core.settings.base import BD_ERROR_MESSAGE, SUCCESS_MESSAGE
from . import models
from .serializers import CategoriaSerializer, CategoriaCrearSerializer
from .models import Categoria


class CategoriaView(GenericViewSet):

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, SuperUsuarioPermission]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, SuperUsuarioPermission]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, SuperUsuarioPermission]
        elif self.action == 'partial_update':
            permission_classes = [IsAuthenticated, SuperUsuarioPermission]
        else:
            permission_classes = [IsAuthenticated, SuperUsuarioPermission]
        return [permission() for permission in permission_classes]

    def retrieve(self):
        try:
            return self.get_object()
        except DatabaseError:
            respuesta = {
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': BD_ERROR_MESSAGE,
                'data': None
            }
            return Response(respuesta, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        try:
            if request.user.is_superuser:
                queryset = models.Categoria.objects.all()
                categorias_serializer = CategoriaSerializer(queryset, many=True)
                respuesta = {
                    'code': status.HTTP_200_OK,
                    'message': SUCCESS_MESSAGE,
                    'data': categorias_serializer.data
                }
                return Response(respuesta, status=status.HTTP_200_OK)
            else:
                queryset = models.Categoria.objects.filter(cat_estado=True)
                categorias_serializer = CategoriaSerializer(queryset, many=True)
                respuesta = {
                    'code': status.HTTP_200_OK,
                    'message': SUCCESS_MESSAGE,
                    'data': categorias_serializer.data
                }
                return Response(respuesta, status=status.HTTP_200_OK)

        except DatabaseError:
            respuesta = {
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': BD_ERROR_MESSAGE,
                'data': None
            }
            return Response(respuesta, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:

            print(request.data)
            crear_categoria_serializer = CategoriaCrearSerializer(data=request.data)
            if crear_categoria_serializer.is_valid():
                crear_categoria_serializer.create(request.data)
                respuesta = {
                    'code': status.HTTP_200_OK,
                    'message': SUCCESS_MESSAGE,
                    'data': crear_categoria_serializer.data
                }
                return Response(respuesta, status=status.HTTP_200_OK)
            else:
                respuesta = {
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': obtenerErrorSerializer(crear_categoria_serializer),
                    'data': None
                }
                return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)

        except DatabaseError:
            respuesta = {
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': BD_ERROR_MESSAGE,
                'data': None
            }
            return Response(respuesta, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):  # Faltaaa
        try:
            if self.get_object():
                print("si entra")
                print(self.get_object())
                categoria_serializer = self.serializer_class(data=request.data)
                if categoria_serializer.is_valid():
                    print('objeto request')
                    print(request.data)
                    categoria_serializer.update(instance=self.get_object(), data=request.data)
                    respuesta = {
                        'code': status.HTTP_200_OK,
                        'message': SUCCESS_MESSAGE,
                        'data': categoria_serializer.data
                    }
                    return Response(respuesta, status=status.HTTP_200_OK)
                else:
                    respuesta = {
                        'code': status.HTTP_400_BAD_REQUEST,
                        'message': obtenerErrorSerializer(categoria_serializer),
                        'data': None
                    }
                    return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
            else:
                respuesta = {
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': "La categoría no existe.",
                    'data': None
                }
                return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)

        except DatabaseError:
            respuesta = {
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': BD_ERROR_MESSAGE,
                'data': None
            }
            return Response(respuesta, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            idCategoria = models.Categoria.objects.get(pk=self.kwargs['pk'])
            idCategoria.delete()
            datos = {'code': status.HTTP_200_OK, 'message': "Categoría Eliminada", 'data': None}
            print("ELIMINACIÓN EXITOSA")
            return Response(datos, status=status.HTTP_200_OK)
        except Categoria.DoesNotExist:
            datos = {'code': status.HTTP_404_NOT_FOUND, 'message': "ID no existe", 'data': None}
            return Response(datos, status=status.HTTP_404_NOT_FOUND)

    def get_object(self):
        try:
            categoria = Categoria.objects.get(pk=self.kwargs['pk'])
            serializer_categoria = CategoriaSerializer(categoria)
            return serializer_categoria.data
        except Categoria.DoesNotExist:
            respuesta = {
                'code': status.HTTP_400_BAD_REQUEST,
                'message': "La categoría no existe.",
                'data': None
            }
            return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
