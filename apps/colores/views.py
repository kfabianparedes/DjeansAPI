from django.shortcuts import render
from django.forms import ValidationError
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import ColorSerializer
from .models import COLOR

# Create your views here.

class ColorAPIView(APIView):
    def get_object(self, pk):
        try:
            return COLOR.objects.get(pk=pk)
        except COLOR.DoesNotExist:
            datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
            return Response(datos,status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        obtenerColor=list(COLOR.objects.values())
        if len(obtenerColor)>0:
            datos={'code':status.HTTP_200_OK,'message':"SOLICITUD EXITOSA",'data':obtenerColor}
            return Response(datos,status= status.HTTP_200_OK)
        else:
            datos={'code':status.HTTP_400_BAD_REQUEST,'message':"NO SE ENCONTRARON REGISTROS",'data':None}
            return Response(datos,status= status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        crearColor=ColorSerializer(data=request.data)
        if crearColor.is_valid():
            crearColor.save()
            datos={'code':status.HTTP_201_CREATED,'message':"CREACIÓN EXITOSA",'data':request.data}
            return Response(datos,status=status.HTTP_201_CREATED)
        else:
            datos={'code':status.HTTP_400_BAD_REQUEST,'message':crearColor._errors.values(),'data':None}
            return Response(datos,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk):
        editarColor= self.get_object(pk)
        serializarColor= ColorSerializer(editarColor,data=request.data)
        if serializarColor.is_valid():
            serializarColor.save()
            datos={'code':status.HTTP_200_OK,'message':"SE EDITÓ CORRECTAMENTE",'data':editarColor}
            return Response(datos, status=status.HTTP_200_OK)
        return Response(serializarColor.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            idColor = COLOR.objects.get(pk=pk)
            idColor.delete()
            datos={'code':status.HTTP_200_OK,'message':"Color Eliminado",'data':None}
            print("ELIMINACIÓN EXITOSA")
            return Response(datos,status=status.HTTP_200_OK)
        except COLOR.DoesNotExist:
            datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
            return Response(datos,status=status.HTTP_404_NOT_FOUND)