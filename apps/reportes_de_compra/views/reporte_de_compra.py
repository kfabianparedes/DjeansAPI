from datetime import date, datetime
from pymysql import DatabaseError
from rest_framework import status
from apps.compras.models import Compra
from apps.reportes_de_compra.serializers.reporteCompra import ReporteCompraSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission
from rest_framework.viewsets import GenericViewSet

from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
# Create your views here.
class ReporteCompraView(GenericViewSet):
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [EstaAutenticadoPermission]
        else:
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        return [permission() for permission in permission_classes]
    def list(self,request,fechaIni,fechaFin):
        try:
            if request.user.is_superuser:
                # fechaIni=datetime.date.__format__('')
                queryset=Compra.objects.filter(comp_fecha_registro__range=(fechaIni,fechaFin))
                reporteCompra_serializer=ReporteCompraSerializer(queryset,many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, reporteCompra_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)