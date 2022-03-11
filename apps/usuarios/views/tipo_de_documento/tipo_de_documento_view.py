from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from apps.usuarios.serializers.tipo_de_documento.tipo_de_documento_serializer import TipoDeDocumentoSerializer
from apps.usuarios.tipo_de_documento_model import TipoDeDocumento
from core.assets.permissions.user_permission import EstaAutenticadoPermission, MetodoSegurosPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class TipoDeDocumentoView(GenericViewSet):
    serializer_class = TipoDeDocumentoSerializer
    permission_classes = [MetodoSegurosPermission, EstaAutenticadoPermission]
    queryset = TipoDeDocumento.objects.all()

    def list(self, request):
        try:
            tipo_documento_serializer = self.serializer_class(self.queryset, many=True)
            return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, tipo_documento_serializer.data)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
