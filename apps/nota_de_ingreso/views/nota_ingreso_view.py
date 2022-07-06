from django.db import transaction
from rest_framework.viewsets import GenericViewSet

from django.db import DatabaseError
from rest_framework import status

from apps.detalles_de_ingreso.serializers.detalle_de_ingreso_serializer import DetalleDeIngresoSerializer
from apps.nota_de_ingreso.models import NotaDeIngreso
from apps.nota_de_ingreso.serializers.nota_de_ingreso_serializer import NotaDeIngresoSerializer
from apps.nota_de_ingreso.serializers.registrar_nota_de_ingreso_serializer import NotaDeIngresoRegistrarSerializer

from apps.usuarios.models import Usuario
from apps.usuarios.serializers.usuario.usuario_serializer import UsuarioSerializer


from apps.compras.serializers.compras_serializer import CompraSerializer
from apps.detalles_de_ingreso.serializers.registrar_detalle_de_ingreso_serializer import DetalleDeIngresoRegistrarSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class NotaDeIngresoView(GenericViewSet):

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [EstaAutenticadoPermission]
        elif self.action == 'create':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'update':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        elif self.action == 'destroy':
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        else:
            permission_classes = [EstaAutenticadoPermission, SuperUsuarioPermission]
        return [permission() for permission in permission_classes]

    def create(self, request):
        try:
            nota_de_ingreso = NotaDeIngresoRegistrarSerializer(data=request.data.get('nota_de_ingreso'))
            if nota_de_ingreso.is_valid():
                with transaction.atomic():
                    nota_de_ingreso.save()
                    last_note = NotaDeIngreso.objects.latest('nota_ingreso_id')
                    nota_ingreso = NotaDeIngresoSerializer(last_note)
                    detalles = request.data.get('detalles')
                    for detail in detalles:
                        detail["nota_de_ingreso"] = nota_ingreso.data.get('nota_ingreso_id')
                        detalle = DetalleDeIngresoRegistrarSerializer(data=detail)
                        if not detalle.is_valid():
                            transaction.set_rollback(rollback=True)
                            return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                                 message=obtenerErrorSerializer(detalle))
                        detalle.save()

                    return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, nota_de_ingreso.data, success=True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=obtenerErrorSerializer(nota_de_ingreso))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)
