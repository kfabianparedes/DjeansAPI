from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from apps.usuarios.clases import TipoDocumento
from rest_framework.generics import ListAPIView

from apps.usuarios.serializers.informacion_personal_serializer import TipoDocumentoSerializar


class TipoDocumento(ListAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializar
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TipoDocumentoSerializar(queryset, many=True)
        respuesta = {
            'code': status.HTTP_200_OK,
            'message': "Solicitud ejecutada con éxito.",
            'data': serializer.data
        }
        return Response(respuesta, status=status.HTTP_200_OK)
