from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser

from apps.sucursales.models import SUCURSALES
from apps.sucursales.serializers import sucursalSerializers


# Create your views here.
class SucursalAPIView(APIView):
    def get(self, request):
        obtenerSucursal = list(SUCURSALES.objects.values())
        if len(obtenerSucursal) > 0:
            datos = {'code': status.HTTP_200_OK, 'message': "Solicitud exitosa", 'data': obtenerSucursal}
            return Response(datos, status=status.HTTP_200_OK)
        else:
            datos = {'code': status.HTTP_400_BAD_REQUEST, 'message': "No hay registro de surcursales", 'data': None}
            return Response(datos, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        registro = sucursalSerializers(data=request.data)
        if registro.is_valid():
            nuevoRegistro = registro.save()
            # id=SUCURSALES.objects.get(pk=nuevoRegistro.pk)
            # print(id)
            datos = {'code': status.HTTP_201_CREATED, 'message': "Creacion exitosa", 'data': request.data}
            return Response(datos, status=status.HTTP_201_CREATED)
        else:
            datos = {'code': status.HTTP_400_BAD_REQUEST, 'message': "Creacion fallada", 'data': None}
            return Response(datos, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # MODIFICAR AL FORMATO DE RESPUESTA 
        try:
            suc = SUCURSALES.objects.get(pk=pk)
        except SUCURSALES.DoesNotExist:
            # return HttpResponse(status=404)
            datos = {'code': status.HTTP_404_NOT_FOUND, 'message': "ID no existe", 'data': None}
            return Response(datos, status=status.HTTP_404_NOT_FOUND)

        datoEdidato = JSONParser().parse(request)
        datoSerializado = sucursalSerializers(suc, data=datoEdidato)
        if datoSerializado.is_valid():
            datoSerializado.save()
            return JsonResponse(datoSerializado.data)
        return JsonResponse(datoSerializado.errors, status=400)

    def delete(self, request, pk):
        idSucursal = SUCURSALES.objects.filter(pk=pk)
        idSucursal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
