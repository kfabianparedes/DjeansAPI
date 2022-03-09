from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from rest_framework.permissions import IsAdminUser, IsAuthenticated , BasePermission


class UsuarioPropioPermission(BasePermission):
    message = 'El usuario solo puede ser actualizado por el mismo.'

    def has_object_permission(self, request, view, obj):

        if bool(obj.user == request.user or request.user.is_superuser):
            return True
        else:
            response = {
                "code": 403,
                'message': self.message,
                "data": None
            }
            raise PermissionDenied(detail=response, code=403)


class SuperUsuarioPermission(IsAdminUser):
    # Declaro la respuesta que deseo para este permiso
    respuesta = {
        "code": 403,
        'message': 'El usuario no es super usuario.',
        "data": None
    }

    def has_permission(self, request, view):
        if bool(request.user.is_superuser):  # Verifico que sea super usuario
            return True
        else:
            # Creo una instancia de PermissionDenied para sobreescribir la respuesta
            permision = PermissionDenied()  # Como hereda de APIException puedo utilizar "detail" para responder
            permision.detail = self.respuesta
            raise permision


class EstaAutenticado(IsAuthenticated):
    # Declaro la respuesta que deseo para este permiso
    respuesta = {
        "code": 401,
        'message': 'El usuario no está autenticado.',
        "data": None
    }

    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):  # Verifico que este autenticado
            return True
        else:
            # Creo una instancia de PermissionDenied para sobreescribir la respuesta
            permision = NotAuthenticated()  # Como hereda de APIException puedo utilizar "detail" para responder
            permision.detail = self.respuesta
            raise permision
