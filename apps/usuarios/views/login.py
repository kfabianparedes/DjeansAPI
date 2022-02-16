from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from apps.usuarios.serializers.serializer import UsuarioTokenSerializer


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid():
            usuario = login_serializer.validated_data['user']
            if usuario.is_active:
                token, existe = Token.objects.get_or_create(user=usuario)
                user_serializer = UsuarioTokenSerializer(usuario)
                if existe:  # Cuando el token existe se retorna e inica sesión
                    respuesta = {
                        'code': status.HTTP_200_OK,
                        'message': "Inicio de Sesión Exitoso.",
                        'data': {
                            'token': token.key,
                            'username': user_serializer.data['username'],
                            'id': user_serializer.data['id'],
                        }
                    }
                    return Response(respuesta, status=status.HTTP_200_OK)
                else:  # Cuando el token no fue creado se crea otro
                    token.delete()
                    token = Token.objects.create(user=usuario)
                    respuesta = {
                        'code': status.HTTP_200_OK,
                        'message': "Inicio de Sesión Exitoso.",
                        'data': {
                            'token': token.key,
                            'username': user_serializer.data['username'],
                            'id': user_serializer.data['id'],
                        }
                    }
                    return Response(respuesta, status=status.HTTP_200_OK)

            else:
                respuesta = {
                    'code': status.HTTP_401_UNAUTHORIZED,
                    'message': "El usuario no está activo, contácte al administrador.",
                    'data': None
                }
                return Response(respuesta, status=status.HTTP_401_UNAUTHORIZED)
        else:
            respuesta = {
                'code': status.HTTP_400_BAD_REQUEST,
                'message': "El nombre de usuario o contraseña son incorrectos.",
                'data': None
            }
            return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
