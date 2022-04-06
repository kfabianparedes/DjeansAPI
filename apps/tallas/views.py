from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import BD_ERROR_MESSAGE, SUCCESS_MESSAGE

from .serializers.create_talla_serializer import CreateTallaSerializer
from .serializers.update_talla_serializer_py import UpdateTallaSerializer
from .serializers.talla_serializer import TallaSerializer
from .serializers.partial_update_talla_serializer import PartialUpdateTallaSerializer

from . import models
from apps.tallas.models import Talla
# Create your views here.


class TallaView(GenericViewSet):

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

    def list(self, request):
        try:
            if request.user.is_superuser:

                queryset = models.Talla.objects.all().order_by('-tal_estado')
                talla_serializer = TallaSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_400_BAD_REQUEST,SUCCESS_MESSAGE,talla_serializer.data,True)

            else:

                queryset = models.Talla.objects.filter(tal_estado=True).order_by('-tal_estado')
                talla_serializer = TallaSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_400_BAD_REQUEST,SUCCESS_MESSAGE,talla_serializer.data,True)

        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)

    def retrieve(self, request, pk=None):
        try:
            tal_id_buscado = self.kwargs['pk']

            if validarEsNumerico(tal_id_buscado) and validarEsMayorQueCero(tal_id_buscado):
                talla_obtenida  = Talla.objects.get(tal_id = tal_id_buscado)
                talla_serializer = TallaSerializer(talla_obtenida)
                return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE,talla_serializer.data,True)

            else:
                mensaje = 'Los parámetros deber ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=mensaje)


        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)

    def create(self, request):
        try:
            create_talla_serializer = CreateTallaSerializer(data=request.data)
            if create_talla_serializer.is_valid():
                create_talla_serializer.create(request.data)
                return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE,create_talla_serializer.data,True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                     message=obtenerErrorSerializer(create_talla_serializer))

        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)

    def update(self, request, pk=None):
        try:
            talla_id_buscado = self.kwargs['pk']
            if validarEsNumerico(talla_id_buscado) and validarEsMayorQueCero(talla_id_buscado):
                talla_obtenida = Talla.objects.get(tal_id = talla_id_buscado)
                if request.data.get('tal_id') == int(talla_id_buscado):
                    talla_serializer = UpdateTallaSerializer(talla_obtenida,data=request.data)
                    if talla_serializer.is_valid():
                        talla_serializer.update(talla_obtenida,request.data)
                        return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE,talla_serializer.data,True)
                    else :
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                             message=obtenerErrorSerializer(talla_serializer))
                else:
                    mensaje = 'Los parámetros y el ID enviado deben coincidir.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=mensaje)
            else:
                mensaje = 'Los parámetros deber ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=mensaje)
        except Talla.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message='La talla no existe.')
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)

    def partial_update(self, request, pk = None):
        try:
            tal_id_buscado = self.kwargs['pk']
            if validarEsNumerico(tal_id_buscado) and validarEsMayorQueCero(tal_id_buscado):
                talla_obtenida = Talla.objects.get(tal_id = tal_id_buscado)
                talla_serializer = UpdateTallaSerializer(talla_obtenida, data = request.data)
                if talla_serializer.is_valid():
                    talla_serializer.update(talla_obtenida,request.data)
                    return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE,talla_serializer.data,True)
                else:
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                         message=obtenerErrorSerializer(talla_serializer))
            else:
                mensaje = 'Los parámetros deber ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=mensaje)
        except Talla.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message="La talla no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)

    def destroy(self, request, pk=None):
        try:
            tal_id_buscado = self.kwargs['pk']
            if validarEsNumerico(tal_id_buscado) and validarEsMayorQueCero(tal_id_buscado):
                talla_obtenida = Talla.objects.get(tal_id = tal_id_buscado)
                talla_actuaizada = TallaSerializer(talla_obtenida)
                talla_obtenida = Talla.objects.filter(tal_id = tal_id_buscado).update(
                    tal_estado = not talla_actuaizada.data.get('tal_estado'))
                if talla_obtenida == 1:
                    return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE,success=True)
                else:
                    mensaje = 'La categoría no existe.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=mensaje)
            else:
                mensaje = 'Los parámetros deber ser numéricos y mayores a 0.'

        except Talla.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message="La talla no existe.")
        except DatabaseError:
            return  respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)


#
# class TallaAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return TALLA.objects.get(pk=pk)
#         except TALLA.DoesNotExist:
#             datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
#             return Response(datos,status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request):
#         obtenerTalla=list(TALLA.objects.values())
#         if len(obtenerTalla)>0:
#             datos={'code':status.HTTP_200_OK,'message':"SOLICITUD EXITOSA",'data':obtenerTalla}
#             return Response(datos,status= status.HTTP_200_OK)
#         else:
#             datos={'code':status.HTTP_400_BAD_REQUEST,'message':"NO SE ENCONTRARON REGISTROS",'data':None}
#             return Response(datos,status= status.HTTP_400_BAD_REQUEST)
#
#     def post(self, request):
#         crearTalla=TallaSerializer(data=request.data)
#         if crearTalla.is_valid():
#             crearTalla.save()
#             datos={'code':status.HTTP_201_CREATED,'message':"CREACIÓN EXITOSA",'data':request.data}
#             return Response(datos,status=status.HTTP_201_CREATED)
#         else:
#             datos={'code':status.HTTP_400_BAD_REQUEST,'message':crearTalla._errors.values(),'data':None}
#             return Response(datos,status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request,pk):
#         editarTalla= self.get_object(pk)
#         serializarTalla= TallaSerializer(editarTalla,data=request.data)
#         if serializarTalla.is_valid():
#             serializarTalla.save()
#             datos={'code':status.HTTP_200_OK,'message':"SE EDITÓ CORRECTAMENTE",'data':editarTalla}
#             return Response(datos, status=status.HTTP_200_OK)
#         return Response(serializarTalla.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk):
#         try:
#             idTalla = TALLA.objects.get(pk=pk)
#             idTalla.delete()
#             datos={'code':status.HTTP_200_OK,'message':"Color Eliminado",'data':None}
#             print("ELIMINACIÓN EXITOSA")
#             return Response(datos,status=status.HTTP_200_OK)
#         except TALLA.DoesNotExist:
#             datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
#             return Response(datos,status=status.HTTP_404_NOT_FOUND)