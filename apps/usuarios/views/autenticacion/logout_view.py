from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.usuarios.models import Usuario
from apps.usuarios.serializers.autenticacion.logout_serializer import LogoutSerializer
from core.assets.permissions.user_permission import MetodoPostSeguroPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import obtenerErrorSerializer


class Logout(GenericAPIView):
    permission_classes = [MetodoPostSeguroPermission]

    def post(self, request):
        username = request.data.get('username', '')
        usu_id = request.data.get('id', 0)
        logout_serializer = LogoutSerializer(data=request.data)
        if logout_serializer.is_valid():  # Validamos los campos ingresados y verificamos que exista el username
            user = Usuario.objects.filter(id=usu_id, username=username)
            if user.exists():
                RefreshToken.for_user(user.first())
                message = "Sesión cerrada correctamente."
                return respuestaJson(status.HTTP_200_OK, message, success=True)
            else:
                message = "No existe este usuario."
                return respuestaJson(status.HTTP_400_BAD_REQUEST, message)
        else:
            return respuestaJson(status.HTTP_400_BAD_REQUEST, obtenerErrorSerializer(logout_serializer))
