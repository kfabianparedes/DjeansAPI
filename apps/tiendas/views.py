from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.tiendas.models import TIENDAS
from apps.tiendas.serializers import tiendasSerializers

# Create your views here.
class TiendaAPIView(APIView):
    def get(self,request):
        pass
    def post(self,request):
        pass
    def put(self,request,pk):
        pass
    def delete(self,request,pk):
        pass