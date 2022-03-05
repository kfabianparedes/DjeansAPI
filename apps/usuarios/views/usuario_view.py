from django.db import DatabaseError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from core.assets.permissions.user_permission import SuperUsuarioPermission, UsuarioPropioPermission, IsAuthenticated
from core.assets.validations.obtener_error_serializer import obtenerErrorSerializer
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE
from ..models import Usuario
from ..serializers.usuario_serializer import UsuarioSerializer, UsuarioRegistrarSerializer


class UsuarioView(GenericViewSet):

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated, SuperUsuarioPermission]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, UsuarioPropioPermission, SuperUsuarioPermission]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, SuperUsuarioPermission]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, SuperUsuarioPermission]
        elif self.action == 'partial_update':
            permission_classes = [IsAuthenticated, UsuarioPropioPermission, SuperUsuarioPermission]
        else:
            permission_classes = [IsAuthenticated, SuperUsuarioPermission]
        return [permission() for permission in permission_classes]

    def create(self, request):
        try:
            user_serializer = UsuarioRegistrarSerializer(data=request.data)
            if user_serializer.is_valid():  # raise_exception=True es para retornar directamente la lista de errores en json
                user_serializer.create(request.data)
                respuesta = {
                    'code': status.HTTP_200_OK,
                    'message': SUCCESS_MESSAGE,
                    'data': user_serializer.data
                }
                return Response(respuesta, status=status.HTTP_200_OK)
            else:
                respuesta = {
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': obtenerErrorSerializer(user_serializer),
                    'data': None
                }
                return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseError:
            respuesta = {
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': BD_ERROR_MESSAGE,
                'data': None
            }
            return Response(respuesta, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        try:
            queryset = Usuario.objects.all()
            serializer = UsuarioSerializer(queryset, many=True)
            return Response(serializer.data)
        except DatabaseError:
            respuesta = {
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': BD_ERROR_MESSAGE,
                'data': None
            }
            return Response(respuesta, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
