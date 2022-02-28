from django.shortcuts import render
from django.forms import ValidationError
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import ModeloSerializer
from .models import MODELO

# Create your views here.
class ModeloAPIView(APIView):
    def get_object(self, pk):
        try:
            return MODELO.objects.get(pk=pk)
        except MODELO.DoesNotExist:
            datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
            return Response(datos,status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        obtenerModelo=list(MODELO.objects.values())
        if len(obtenerModelo)>0:
            datos={'code':status.HTTP_200_OK,'message':"SOLICITUD EXITOSA",'data':obtenerModelo}
            return Response(datos,status= status.HTTP_200_OK)
        else:
            datos={'code':status.HTTP_400_BAD_REQUEST,'message':"NO SE ENCONTRARON REGISTROS",'data':None}
            return Response(datos,status= status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        crearModelo=ModeloSerializer(data=request.data)
        if crearModelo.is_valid():
            crearModelo.save()
            datos={'code':status.HTTP_201_CREATED,'message':"CREACIÓN EXITOSA",'data':request.data}
            return Response(datos,status=status.HTTP_201_CREATED)
        else:
            datos={'code':status.HTTP_400_BAD_REQUEST,'message':crearModelo._errors.values(),'data':None}
            return Response(datos,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk):
        editarModelo= self.get_object(pk)
        serializarModelo= ModeloSerializer(editarModelo,data=request.data)
        if serializarModelo.is_valid():
            serializarModelo.save()
            datos={'code':status.HTTP_200_OK,'message':"SE EDITÓ CORRECTAMENTE",'data':editarModelo}
            return Response(datos, status=status.HTTP_200_OK)
        return Response(serializarModelo.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            idModelo = MODELO.objects.get(pk=pk)
            idModelo.delete()
            datos={'code':status.HTTP_200_OK,'message':"Modelo Eliminado",'data':None}
            print("ELIMINACIÓN EXITOSA")
            return Response(datos,status=status.HTTP_200_OK)
        except MODELO.DoesNotExist:
            datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
            return Response(datos,status=status.HTTP_404_NOT_FOUND)