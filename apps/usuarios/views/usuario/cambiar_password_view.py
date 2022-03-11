from django.db import DatabaseError
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from core.assets.permissions.user_permission import *
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE
from apps.usuarios.models import Usuario
from apps.usuarios.serializers.usuario.password_serializer import PasswordSerializer


class PasswordView(GenericViewSet):

    def get_permissions(self):
        if self.action == 'partial_update':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        else:
            permission_classes = [EstaAutenticadoPermission, MetodoNoPermitidoPermission]
        return [permission() for permission in permission_classes]

    def partial_update(self, request, pk=None):
        try:
            usu_id = self.kwargs['pk']
            if validarEsNumerico(usu_id) and validarEsMayorQueCero(usu_id):
                usuario_obtenido = Usuario.objects.get(id=usu_id)
                print('usuario obtenido:')
                print(usuario_obtenido)
                if request.data.get('id') == int(usu_id):
                    password_serializer = PasswordSerializer(data=request.data)
                    if password_serializer.is_valid():
                        if usuario_obtenido.check_password(request.data.get('old_password')):
                            user = Usuario.objects.filter(id=usu_id, username=usuario_obtenido)
                            if user.exists():
                                RefreshToken.for_user(user.first())  # Actualiza el token del usuario
                                password_serializer.update(usuario_obtenido, request.data)
                                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE)
                            else:
                                mensaje = "Hubo un error actualizando la contraseña. No se pudo obtener el usuario."
                                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
                        else:
                            mensaje = "La contraseña antigua es incorrecta."
                            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
                    else:
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=obtenerErrorSerializer(password_serializer))
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
