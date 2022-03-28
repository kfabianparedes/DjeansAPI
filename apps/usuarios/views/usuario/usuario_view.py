from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from core.assets.permissions.user_permission import *
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import obtenerErrorSerializer, validarEsNumerico, validarEsMayorQueCero
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE
from apps.usuarios.models import Usuario
from apps.usuarios.serializers.usuario.usuario_serializer import UsuarioSerializer
from apps.usuarios.serializers.usuario.usuario_actualizar_serializer import UsuarioActualizarSerializer
from apps.usuarios.serializers.usuario.usuario_registro_serializer import UsuarioRegistrarSerializer


class UsuarioView(GenericViewSet):

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'retrieve':
            permission_classes = [EstaAutenticadoPermission, UsuarioPropioPermission]
        elif self.action == 'create':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'update':
            permission_classes = [EstaAutenticadoPermission, UsuarioPropioPermission]
        else:
            permission_classes = [EstaAutenticadoPermission, MetodoNoPermitidoPermission]
        return [permission() for permission in permission_classes]

    def create(self, request):
        try:
            user_serializer = UsuarioRegistrarSerializer(data=request.data)
            if user_serializer.is_valid():  # raise_exception=True es para retornar directamente la lista de errores en json
                user_serializer.create(request.data)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, user_serializer.data, True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=obtenerErrorSerializer(user_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def list(self, request):
        try:
            queryset = Usuario.objects.all().exclude(username=request.user)
            user_serializer = UsuarioSerializer(queryset, many=True)
            return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, user_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def retrieve(self, request, pk=None):
        try:

            usu_id = self.kwargs['pk']
            if validarEsNumerico(usu_id) and validarEsMayorQueCero(usu_id):
                usuario_obtenido = Usuario.objects.get(id=usu_id)
                usuario_serializer = UsuarioSerializer(usuario_obtenido)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, usuario_serializer.data, True)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Usuario.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="El usuario no está registrado.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
        
    def update(self, request, pk=None):
        try:
            usu_id = self.kwargs['pk']
            if validarEsNumerico(usu_id) and validarEsMayorQueCero(usu_id):
                usuario_obtenido = Usuario.objects.get(id=usu_id)
                if request.data.get('id') == int(usu_id):
                    usuario_serializer = UsuarioActualizarSerializer(usuario_obtenido, data=request.data)
                    if usuario_serializer.is_valid():
                        usuario_serializer.update(usuario_obtenido, request.data)
                        return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, usuario_serializer.data, True)
                    else:
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=obtenerErrorSerializer(usuario_serializer))
                else:
                    mensaje = 'Los parámetros y el ID enviado deben coincidir.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Usuario.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="El usuario no está registrado.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
        
        
    def destroy(self, request, pk=None):
        try:
            usu_id_buscado = self.kwargs['pk']
            if validarEsNumerico(usu_id_buscado) and validarEsMayorQueCero(usu_id_buscado):
                usuario_obtenido = Categoria.objects.filter(id=usu_id_buscado).update(cat_estado=False)
                print(usuario_obtenido)
                if usuario_obtenido == 1:
                    return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, message=True)
                else:
                    mensaje = 'La categoría no existe.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Categoria.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="La categoría no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)