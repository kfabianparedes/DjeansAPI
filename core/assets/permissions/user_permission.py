from rest_framework import permissions, status
from rest_framework.exceptions import PermissionDenied, NotAuthenticated, MethodNotAllowed
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission


class UsuarioPropioPermission(BasePermission):
    message = 'El usuario solo puede ser actualizado por el mismo.'
    response = {"code": status.HTTP_403_FORBIDDEN,'message': message,"data": None}

    def has_object_permission(self, request, view, obj):
        if bool(obj.user == request.user or request.user.is_superuser):
            return True
        else:
            # Creo una instancia de PermissionDenied para sobreescribir la respuesta
            permision = PermissionDenied()  # Como hereda de APIException puedo utilizar "detail" para responder
            permision.detail = self.respuesta
            raise permision

class SuperUsuarioPermission(IsAdminUser):
    # Declaro la respuesta que deseo para este permiso
    respuesta = {
        "code": status.HTTP_403_FORBIDDEN,
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


class EstaAutenticadoPermission(IsAuthenticated):
    # Declaro la respuesta que deseo para este permiso
    respuesta = {
        "code": status.HTTP_401_UNAUTHORIZED,
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


class MetodoSegurosPermission(BasePermission):
    respuesta = {
        "code": status.HTTP_405_METHOD_NOT_ALLOWED,
        'message': 'Método HTTP no permitido.',
        "data": None
    }

    def has_permission(self, request, view):
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            # Creo una instancia de PermissionDenied para sobreescribir la respuesta
            permision = MethodNotAllowed(method=request.method)
            permision.detail = self.respuesta
            raise permision

class MetodoNoPermitidoPermission(BasePermission):
    respuesta = {
        "code": status.HTTP_405_METHOD_NOT_ALLOWED,
        'message': 'Método HTTP no permitido.',
        "data": None
    }
    def has_permission(self, request, view):
        permision = MethodNotAllowed(method=request.method)
        permision.detail = self.respuesta
        raise permision

class MetodoPostSeguroPermission(BasePermission):
    respuesta = {
        "code": status.HTTP_405_METHOD_NOT_ALLOWED,
        'message': 'Método HTTP no permitido.',
        "data": None
    }
    def has_permission(self, request, view):
        if request.method == 'POST' or request.method =='OPTIONS' or request.method == 'HEADS':
            return True
        permision = MethodNotAllowed(method=request.method)
        permision.detail = self.respuesta
        raise permision