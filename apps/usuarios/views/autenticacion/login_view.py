from django.contrib.auth import authenticate
from django.db import DatabaseError
from django.utils import timezone
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.usuarios.models import Usuario
from apps.roles.models import Rol
from apps.roles.serializers.rol_serializer import RolSerializer
from apps.usuarios.serializers.autenticacion.login_serializer import LoginSerializer
from apps.usuarios.serializers.usuario.usuario_serializer import UsuarioSerializer
from core.assets.permissions.user_permission import *
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import obtenerErrorSerializer
from core.settings.base import BD_ERROR_MESSAGE


class Login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    permission_classes = [MetodoPostSeguroPermission]

    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            login_serializer = LoginSerializer(data=request.data)
            if login_serializer.is_valid():  # Validamos los campos ingresados y verificamos que exista el username
                user = authenticate(username=username, password=password)
                if user:  # Si la autenticación es correcta retorna el "username" sino "None"
                    login_serializer = self.serializer_class(data=request.data)
                    if login_serializer.is_valid():  # and
                        if login_serializer.validated_data.get('access') and login_serializer.validated_data.get(
                                'refresh'):
                            usuario = Usuario.objects.filter(username=user).update(last_login=timezone.now())
                            mensaje = "Inicio de Sesión Exitoso."
                            if usuario != 1:
                                mensaje += " No se pudo actualizar el último inicio de sesión."
                            user_serializer = UsuarioSerializer(user)
                            rol = Rol.objects.get(rol_id=user_serializer.data.get('rol'));
                            print(rol)
                            role = RolSerializer(rol)
                            print(role.data)
                            data = {
                                'access': login_serializer.validated_data.get('access'),
                                'refresh': login_serializer.validated_data.get('refresh'),
                                'username': user_serializer.data.get('username'),
                                'id': user_serializer.data.get('id'),
                                'rol': user_serializer.data.get('rol'),
                                'tipoRol': role.data.get('rol_tipo'),
                            }
                            return respuestaJson(status.HTTP_200_OK, mensaje, data, True)
                        else:
                            mensaje = "Hubo un error al obtener los tokens de autorización."
                            return respuestaJson(code=status.HTTP_401_UNAUTHORIZED, message=mensaje)
                    else:
                        mensaje = "Hubo un error al obtener los tokens de autorización."
                        return respuestaJson(code=status.HTTP_401_UNAUTHORIZED, message=mensaje)
                else:
                    mensaje = "Las credenciales son incorrectas o el usuario no está activo, Póngase en contacto con el administrador."
                    return respuestaJson(code=status.HTTP_401_UNAUTHORIZED, message=mensaje)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=obtenerErrorSerializer(login_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
