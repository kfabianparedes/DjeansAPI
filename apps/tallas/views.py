from django.shortcuts import render
from django.forms import ValidationError
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import TallaSerializer
from .models import TALLA

# Create your views here.
class TallaAPIView(APIView):
    def get_object(self, pk):
        try:
            return TALLA.objects.get(pk=pk)
        except TALLA.DoesNotExist:
            datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
            return Response(datos,status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        obtenerTalla=list(TALLA.objects.values())
        if len(obtenerTalla)>0:
            datos={'code':status.HTTP_200_OK,'message':"SOLICITUD EXITOSA",'data':obtenerTalla}
            return Response(datos,status= status.HTTP_200_OK)
        else:
            datos={'code':status.HTTP_400_BAD_REQUEST,'message':"NO SE ENCONTRARON REGISTROS",'data':None}
            return Response(datos,status= status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        crearTalla=TallaSerializer(data=request.data)
        if crearTalla.is_valid():
            crearTalla.save()
            datos={'code':status.HTTP_201_CREATED,'message':"CREACIÓN EXITOSA",'data':request.data}
            return Response(datos,status=status.HTTP_201_CREATED)
        else:
            datos={'code':status.HTTP_400_BAD_REQUEST,'message':crearTalla._errors.values(),'data':None}
            return Response(datos,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk):
        editarTalla= self.get_object(pk)
        serializarTalla= TallaSerializer(editarTalla,data=request.data)
        if serializarTalla.is_valid():
            serializarTalla.save()
            datos={'code':status.HTTP_200_OK,'message':"SE EDITÓ CORRECTAMENTE",'data':editarTalla}
            return Response(datos, status=status.HTTP_200_OK)
        return Response(serializarTalla.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            idTalla = TALLA.objects.get(pk=pk)
            idTalla.delete()
            datos={'code':status.HTTP_200_OK,'message':"Color Eliminado",'data':None}
            print("ELIMINACIÓN EXITOSA")
            return Response(datos,status=status.HTTP_200_OK)
        except TALLA.DoesNotExist:
            datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
            return Response(datos,status=status.HTTP_404_NOT_FOUND)