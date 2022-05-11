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
        elif self.action == 'create':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'update':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'destroy':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        else:
            permission_classes = [MetodoNoPermitidoPermission]
        return [permission() for permission in permission_classes]

    def create(self, request):
        try:
            user_serializer = UsuarioRegistrarSerializer(data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, success=True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=obtenerErrorSerializer(user_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def list(self, request):
        try:
            queryset = Usuario.objects.all().exclude(username=request.user).order_by('-is_active')
            user_serializer = UsuarioSerializer(queryset, many=True)
            return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, user_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def update(self, request, pk=None):
        try:
            print(request.data)
            usu_id = self.kwargs['pk']
            if validarEsNumerico(usu_id) and validarEsMayorQueCero(usu_id):
                usuario_obtenido = Usuario.objects.get(id=usu_id)
                if request.data.get('id') == int(usu_id):
                    usuario_serializer = UsuarioActualizarSerializer(usuario_obtenido, data=request.data)
                    if usuario_serializer.is_valid():
                        usuario_serializer.update(instance=usuario_obtenido, data=request.data)
                        return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, success=True)
                    else:
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=obtenerErrorSerializer(usuario_serializer))
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
                usuario_obtenido = Usuario.objects.get(id=usu_id_buscado)
                usuario_actualizado = UsuarioSerializer(usuario_obtenido)
                filas_modificadas = Usuario.objects.filter(id=usu_id_buscado).update(
                    is_active=not usuario_actualizado.data.get('is_active'))
                if filas_modificadas == 1:
                    return respuestaJson(status.HTTP_202_ACCEPTED, SUCCESS_MESSAGE, success=True)
                else:
                    mensaje = 'El Usuario no existe o no se ha podido desactivar/activar.'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
        except Usuario.DoesNotExist:
            return respuestaJson(status.HTTP_400_BAD_REQUEST, "El usuario no éxiste.")
        except DatabaseError:
            return respuestaJson(status.HTTP_500_INTERNAL_SERVER_ERROR, BD_ERROR_MESSAGE)

        

