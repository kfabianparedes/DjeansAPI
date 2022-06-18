from datetime import date, datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action

from django.db import DatabaseError
from rest_framework import status
from apps.compras.models import Compra
from apps.compras.serializers.compras_serializer import CompraSerializer
from apps.reportes_de_compra.serializers.filtro_reporteCompra import FiltroReporteSucursal
from apps.reportes_de_compra.serializers.reporteCompra import ReporteCompraSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission
from rest_framework.viewsets import GenericViewSet

from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import obtenerErrorSerializer
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
# Create your views here.
class ReporteCompraView(GenericViewSet):
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [EstaAutenticadoPermission]
        # elif self.action == 'retrive':
        #     permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        else:
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        return [permission() for permission in permission_classes]
    def list(self,request):
        try:
            if request.user.is_superuser:
                # fechaIni=datetime.date.__format__('')
                # print("FECHA INICIAL ",fechaIni)
                print("XXXXXXXXXXXXXXXXXX")
                fechaIni=request.query_params.get('fechaIni',None)
                fechaFin=request.query_params.get('fechaFin',None)
                # fechaIni='2022-04-04'
                # fechaFin='2022-06-30'
                fechaActual=datetime.today().strftime('%Y-%m-%d')
                print("FECHA ACTUAL ----> ", fechaActual)
                listaTotal=Compra.objects.filter(comp_fecha_registro__range=(fechaIni,fechaFin))
                reporteCompra_serializer=CompraSerializer(listaTotal,many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, reporteCompra_serializer.data, True)        
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)
    
    # @action(detail=True, methods=['post'])
    def create(self,request):
        try:
            if request.user.is_superuser:
                print("entra a la funcion post")
                fechaIni='2022-05-01'
                fechaFin='2022-05-05'
                listaTotal=Compra.objects.filter(comp_fecha_registro__range=(fechaIni,fechaFin))
                reporteCompra_serializer=ReporteCompraSerializer(listaTotal,many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, reporteCompra_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)

        # listaTotal=Compra.objects.all()
            # objetoSerializadorFiltro=FiltroReporteSucursal(listaTotal,data=fechaIni)
        
            # filter_backends=[DjangoFilterBackend]
            # filterset_fields=['comp_fecha_registro']
        

        
        # METODO 2
        # print("entra a la funcion post")
        # listaTotal=Compra.objects.all()
        # print("va al objetoserializadorFiltro")
        # objetoSerializadorFiltro=FiltroReporteSucursal(listaTotal,data=fechaIni)
        # if objetoSerializadorFiltro.is_valid():
        #     print("Entro al IF")
        #     listaTotal=Compra.objects.filter(comp_fecha_registro__range=(fechaIni,'2022-05-30'))
        #     return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, objetoSerializadorFiltro.data, True)
        # else:
        #     print("paso al else")
        #     return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
        #                                     message=obtenerErrorSerializer(objetoSerializadorFiltro))