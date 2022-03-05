from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.usuarios.models import Usuario
from apps.usuarios.serializers.auth_serializer import UsuarioTokenSerializer, ObtenerTokenSerializer


class Login(TokenObtainPairView):
    serializer_class = ObtenerTokenSerializer

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        if len(username) <= 0 or username == '' or username is None:
            respuesta = {
                'code': status.HTTP_400_BAD_REQUEST,
                'message': "El nombre de usuario es obligatorio.",
                'data': None
            }
            return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
        if len(password) <= 0 or password == '' or password is None:
            respuesta = {
                'code': status.HTTP_400_BAD_REQUEST,
                'message': "La contraseña es obligatoria.",
                'data': None
            }
            return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)

        # Luego de validar los campos se autentica y retorna el username
        user = authenticate(username=username, password=password)

        if user:  # Si la autenticación es correcta retorna el "username" sino "None"
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UsuarioTokenSerializer(user)
                respuesta = {
                    'code': status.HTTP_200_OK,
                    'message': "Inicio de Sesión Exitoso.",
                    'data': {
                        'token': login_serializer.validated_data.get('access'),
                        'refresh_token': login_serializer.validated_data.get('refresh'),
                        'username': user_serializer.data.get('username'),
                        'id': user_serializer.data.get('id'),
                    }
                }
                return Response(respuesta, status=status.HTTP_200_OK)
            else:
                respuesta = {
                    'code': status.HTTP_401_UNAUTHORIZED,
                    'message': "Inicio de Sesión Exitoso.",
                    'data': None
                }
                return Response(respuesta, status=status.HTTP_401_UNAUTHORIZED)
        else:
            respuesta = {
                'code': status.HTTP_401_UNAUTHORIZED,
                'message': "Las credenciales son incorrectas o el usuario no está activo, contácte al administrador.",
                'data': None
            }
            return Response(respuesta, status=status.HTTP_401_UNAUTHORIZED)


class Logout(GenericAPIView):
    def post(self, request):
        username = request.data.get('username', '')
        usu_id = request.data.get('id', 0)
        if len(str.strip(username)) == 0 or username == '' or username is None:
            respuesta = {
                'code': status.HTTP_400_BAD_REQUEST,
                'message': "El nombre de usuario es obligatorio.",
                'data': None
            }
            return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
        if usu_id is None or int(usu_id) <= 0:
            respuesta = {
                'code': status.HTTP_400_BAD_REQUEST,
                'message': "El ID de usuario es obligatorio y un número mayor a 0.",
                'data': None
            }
            return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)

        user = Usuario.objects.filter(id=usu_id, username=username)

        if user.exists():
            RefreshToken.for_user(user.first())
            respuesta = {
                'code': status.HTTP_200_OK,
                'message': "Sesión cerrada correctamente.",
                'data': None
            }
            return Response(respuesta, status=status.HTTP_200_OK)
        else:
            respuesta = {
                'code': status.HTTP_400_BAD_REQUEST,
                'message': "No existe este usuario.",
                'data': None
            }
            return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
