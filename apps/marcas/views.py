from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser 
from rest_framework import status

from apps.marcas.models import MARCAS
from apps.marcas.serializers import marcaSerializers

# Create your views here.
class MarcaAPIView(APIView):
    def get(self,request):
        obtenerSucursal=list(MARCAS.objects.values())
        if len(obtenerSucursal)>0:
            datos={'code':status.HTTP_200_OK,'message':"Solicitud exitosa",'data':obtenerSucursal}
            return Response(datos,status= status.HTTP_200_OK)
        else:
            datos={'code':status.HTTP_400_BAD_REQUEST,'message':"No hay registro de marcas",'data':None}
            return Response(datos,status= status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        registro=marcaSerializers(data=request.data)
        if registro.is_valid():
            nuevoRegistro=registro.save()
            datos={'code':status.HTTP_201_CREATED,'message':"Creacion exitosa",'data':request.data}
            return Response(datos,status=status.HTTP_201_CREATED)
        else:
            datos={'code':status.HTTP_400_BAD_REQUEST,'message':registro._errors.values(),'data':None}
            return Response(datos,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        # MODIFICAR AL FORMATO DE RESPUESTA 
        try:
            suc = MARCAS.objects.get(pk=pk)
        except MARCAS.DoesNotExist:
            datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
            return Response(datos,status=status.HTTP_404_NOT_FOUND)
        datoEdidato=JSONParser().parse(request)
        datoSerializado=marcaSerializers(suc,data=datoEdidato)
        if datoSerializado.is_valid():
            datoSerializado.save()
            # return JsonResponse(datoSerializado.data)
            datos={'code':status.HTTP_200_OK,'message':"SE EDITO CORRECTO",'data':datoEdidato}
            return Response(datos,status=status.HTTP_200_OK)
        else:
            # revisar el mensaje cuando no es valido
            # 'message':datoSerializado.error_messages
            datos={'code':status.HTTP_500_INTERNAL_SERVER_ERROR,'message':datoSerializado.errors.values(),'data':None}
            return Response(datos,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self,request,pk):
        try:
            idSucursal = MARCAS.objects.get(pk=pk)
            idSucursal.delete()
            datos={'code':status.HTTP_200_OK,'message':"Marca Eliminada",'data':None}
            print("TERMINA DE ELIMINAR")
            return Response(datos,status=status.HTTP_200_OK)
        except MARCAS.DoesNotExist:
            datos={'code':status.HTTP_404_NOT_FOUND,'message':"ID no existe",'data':None}
            return Response(datos,status=status.HTTP_404_NOT_FOUND)
