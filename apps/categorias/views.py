from django.forms import ValidationError
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import CategoriaSerializer
from .models import Categoria


# Create your views here.

class CategoriaAPIView(APIView):
#LISTAR CATEGORIA
    def get_object(self, pk):
        try:
            return Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
            return Response(datos,status=status.HTTP_404_NOT_FOUND)

    def get(self,request):
        obtenerCategoria=list(Categoria.objects.values())
        if len(obtenerCategoria)>0:
            datos={'code':status.HTTP_200_OK,'message':"SOLICITUD EXITOSA",'data':obtenerCategoria}
            return Response(datos,status= status.HTTP_200_OK)
        else:
            datos={'code':status.HTTP_400_BAD_REQUEST,'message':"NO SE ENCONTRARON REGISTROS",'data':None}
            return Response(datos,status= status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        crearCategoria=CategoriaSerializer(data=request.data)
        if crearCategoria.is_valid():
            crearCategoria.save()
            datos={'code':status.HTTP_201_CREATED,'message':"CREACIÓN EXITOSA",'data':request.data}
            return Response(datos,status=status.HTTP_201_CREATED)
        else:
            datos={'code':status.HTTP_400_BAD_REQUEST,'message':crearCategoria._errors.values(),'data':None}
            return Response(datos,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        #try:
        #    cat = Categoria.objects.get(pk=pk)
        #except Categoria.DoesNotExist:
        #    datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
        #    return Response(datos,status=status.HTTP_404_NOT_FOUND)
        #editarCategoria=JSONParser().parse(request)
        #serializarCategoria=CategoriaSerializer(cat,data=editarCategoria)
        #if serializarCategoria.is_valid():
        #    serializarCategoria.save()
        #    datos={'code':status.HTTP_200_OK,'message':"SE EDITÓ CORRECTAMENTE",'data':editarCategoria}
        #    return Response(datos,status=status.HTTP_200_OK)
        #else:
        #    datos={'code':status.HTTP_500_INTERNAL_SERVER_ERROR,'message':serializarCategoria.errors.values(),'data':None}
        #    return Response(datos,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        editarCategoria= self.get_object(pk)
        serializarCategoria= CategoriaSerializer(editarCategoria,data=request.data)
        if serializarCategoria.is_valid():
            serializarCategoria.save()
            datos={'code':status.HTTP_200_OK,'message':"SE EDITÓ CORRECTAMENTE",'data':editarCategoria}
            return Response(datos, status=status.HTTP_200_OK)
        return Response(serializarCategoria.errors, status=status.HTTP_400_BAD_REQUEST)

    #ELIMINAR CATEGORIA
    def delete(self,request,pk):
        try:
            idCategoria = Categoria.objects.get(pk=pk)
            idCategoria.delete()
            datos={'code':status.HTTP_200_OK,'message':"Categoría Eliminada",'data':None}
            print("ELIMINACIÓN EXITOSA")
            return Response(datos,status=status.HTTP_200_OK)
        except Categoria.DoesNotExist:
            datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
            return Response(datos,status=status.HTTP_404_NOT_FOUND)