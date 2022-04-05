from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from django.db import DatabaseError
from rest_framework.viewsets import GenericViewSet

from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission
from core.assets.validations.obtener_error_serializer import obtenerErrorSerializer
from core.settings.base import BD_ERROR_MESSAGE, SUCCESS_MESSAGE
#serializer
from .serializers.create_color_serializer import CreateColorSerializer
from .serializers.color_serializer import ColorSerializer
from .serializers.update_color_serializer import UpdateColorSerializer
from .serializers.partial_update_color_serializer import PartialUpdateColorSerializer

#modelos
from apps.colores.models import Color
from . import models

#respuesta json

from core.assets.reutilizable.funciones_reutilizables import respuestaJson

# Create your views here.


class ColorView(GenericViewSet):

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [EstaAutenticadoPermission]
        elif self.action == 'retrieve':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'create':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'update':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'partial_update':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        else:
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        return [permission() for permission in permission_classes]

    def list(self, request):#Falta probar
        try:
            if request.user.is_superuser:
                queryset = models.Color.objects.all().order_by('-col_estado')
                color_serializer = ColorSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE, color_serializer.data, True)
            else:
                queryset = models.Color.objects.filter(cat_estado=True).order_by('-col_estado')
                color_serializer = ColorSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE, color_serializer.data, True)

        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)

    def retrieve(self, request, pk=None):  # FALTA PROBAR
        try:
            col_id_buscado = self.kwargs['pk']
            if validarEsNumerico(col_id_buscado) and validarEsMayorQueCero(col_id_buscado):
                color_obtenido = Color.objects.get(col_id=col_id_buscado)
                color_serializer = ColorSerializer(color_obtenido)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, color_serializer.data, True)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=mensaje)
        except Color.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="El color no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def create(self, request): #FALTA PROBAR
        try:
            create_color_serializer = CreateColorSerializer(data=request.data)
            if create_color_serializer.is_valid():
                create_color_serializer.create(request.data)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE,create_color_serializer.data,
                                     True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                     message=obtenerErrorSerializer(create_color_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)

    def update(self, request, pk=None): # FALTA PROBAR
        try:
            col_id_buscado = self.kwargs['pk']
            if validarEsNumerico(col_id_buscado) and validarEsMayorQueCero(col_id_buscado):
                color_obtenido = Color.objects.get(col_id = col_id_buscado)
                if request.data.get('col_id') == int(col_id_buscado):
                    color_serializer = UpdateColorSerializer(color_obtenido,data=request.data)
                    if color_serializer.is_valid():
                        color_serializer.update(color_obtenido, request.data)
                        return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE,color_serializer.data,True)

                    else:
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                             message=obtenerErrorSerializer(color_serializer))
                else:
                    mensaje = "Los parámetros y el ID enviado deben coincidir."
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Color.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message="El color no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)

    def partial_update(self, request, pk=None):
        try:
            col_id_obtenido = self.kwargs['pk']
            if validarEsNumerico(col_id_obtenido) and validarEsMayorQueCero(col_id_obtenido):
                color_obtenido = Color.objects.get(col_id = col_id_obtenido)
                color_serializer = PartialUpdateColorSerializer(color_obtenido, data=request.data)
                if color_serializer.is_valid():
                    color_serializer.update(color_obtenido, request.data)
                    return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE,color_serializer.data,True)
                else:
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                         message=obtenerErrorSerializer(color_serializer))
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'

        except Color.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message="El color no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)

    def destroy(self, request, pk=None):
        try:
            col_id_obtenido = self.kwargs['pk']
            if validarEsNumerico(col_id_obtenido) and validarEsMayorQueCero(col_id_obtenido):
                color_obtenido = Color.objects.get(col_id = col_id_obtenido)
                color_actuaizado = ColorSerializer(color_obtenido)
                color_obtenido  = Color.objects.filter(col_id=col_id_obtenido).update(
                    col_estado =not color_actuaizado.data.get('col_estado')
                )
                print ("hola")
                if color_obtenido == 1:
                    return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE,success=True)
                else:
                    mensaje = 'El color no existe.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=mensaje)

        except Color.DoesNotExist:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message="El color no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)
    # def get_object(self): #falta mejorar
    #     try:
    #         color = Color.objects.get(pk=self.kwargs['pk'])
    #         serializer_color = ColorSerializer(color)
    #         return serializer_color.data
    #     except Color.DoesNotExist:
    #         respuesta = {
    #             'code': status.HTTP_400_BAD_REQUEST,
    #             'message': "La categoría no existe.",
    #             'data': None
    #         }
    #         return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
    # def get_object(self, pk):
    #     try:
    #         return COLOR.objects.get(pk=pk)
    #     except COLOR.DoesNotExist:
    #         datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
    #         return Response(datos,status=status.HTTP_404_NOT_FOUND)
    #
    # def get(self, request):
    #     obtenerColor=list(COLOR.objects.values())
    #     if len(obtenerColor)>0:
    #         datos={'code':status.HTTP_200_OK,'message':"SOLICITUD EXITOSA",'data':obtenerColor}
    #         return Response(datos,status= status.HTTP_200_OK)
    #     else:
    #         datos={'code':status.HTTP_400_BAD_REQUEST,'message':"NO SE ENCONTRARON REGISTROS",'data':None}
    #         return Response(datos,status= status.HTTP_400_BAD_REQUEST)
    #
    # def post(self, request):
    #     crearColor=ColorSerializer(data=request.data)
    #     if crearColor.is_valid():
    #         crearColor.save()
    #         datos={'code':status.HTTP_201_CREATED,'message':"CREACIÓN EXITOSA",'data':request.data}
    #         return Response(datos,status=status.HTTP_201_CREATED)
    #     else:
    #         datos={'code':status.HTTP_400_BAD_REQUEST,'message':crearColor._errors.values(),'data':None}
    #         return Response(datos,status=status.HTTP_400_BAD_REQUEST)
    #
    # def put(self, request,pk):
    #     editarColor= self.get_object(pk)
    #     serializarColor= ColorSerializer(editarColor,data=request.data)
    #     if serializarColor.is_valid():
    #         serializarColor.save()
    #         datos={'code':status.HTTP_200_OK,'message':"SE EDITÓ CORRECTAMENTE",'data':editarColor}
    #         return Response(datos, status=status.HTTP_200_OK)
    #     return Response(serializarColor.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self,request,pk):
    #     try:
    #         idColor = COLOR.objects.get(pk=pk)
    #         idColor.delete()
    #         datos={'code':status.HTTP_200_OK,'message':"Color Eliminado",'data':None}
    #         print("ELIMINACIÓN EXITOSA")
    #         return Response(datos,status=status.HTTP_200_OK)
    #     except COLOR.DoesNotExist:
    #         datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
    #         return Response(datos,status=status.HTTP_404_NOT_FOUND)