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
            datos={'mensaje':"Exitoso",'resultado':obtenerSucursal}
        else:
            datos={'mensaje':"Error"}
        return JsonResponse(datos)
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