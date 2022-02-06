from itertools import product
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CategoriaSerializer
from .models import Categoria


# Create your views here.

#LISTAR CATEGORIA
@api_view(['GET'])
def ShowAll(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many= True)
    return Response(serializer.data)

#VER DETALLE CATEGORIA x ID
@api_view(['GET'])
def ViewCategoria(request,pk):
    categorias = Categoria.objects.get(CAT_ID=pk)
    serializer = CategoriaSerializer(categorias, many= False)
    return Response(serializer.data)
    

#CREAR CATEGORIA
@api_view(['POST'])
def CreateCategoria(request):
    serializer = CategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#ACTUALIZAR CATEGORIA
@api_view(['POST'])
def UpdateCategoria(request,pk):
    categorias = Categoria.objects.get(CAT_ID=pk)
    serializer = CategoriaSerializer(instance=categorias, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
#ELIMINAR CATEGORIA
@api_view(['GET'])
def DeleteCategoria(request,pk):
    categorias = Categoria.objects.get(CAT_ID=pk)
    categorias.delete()
    return Response('Eliminación exitosa')
    