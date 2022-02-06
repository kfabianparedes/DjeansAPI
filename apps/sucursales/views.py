from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.sucursales.models import SUCURSALES
from apps.sucursales.serializers import sucursalSerializers

# Create your views here.
class SucursalAPIView(APIView):
    def get(self,request):
        obtenerSucursal=list(SUCURSALES.objects.values())
        if len(obtenerSucursal)>0:
            datos={'code':status.HTTP_200_OK,'message':"Solicitud exitosa",'data':obtenerSucursal}
            return Response(datos,status= status.HTTP_200_OK)
        else:
            datos={'code':status.HTTP_400_BAD_REQUEST,'message':"No hay registro de surcursales",'data':None}
            return Response(datos,status= status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        registro=sucursalSerializers(data=request.data)
        if registro.is_valid():
            nuevoRegistro=registro.save()
            # id=SUCURSALES.objects.get(pk=nuevoRegistro.pk)
            # print(id)
            return Response(registro.data,status=status.HTTP_201_CREATED)
        else:
            return Response(registro.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        pass
    def delete(self,request,pk):
        pass