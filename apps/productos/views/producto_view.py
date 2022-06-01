from django.db import DatabaseError
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from django.db import transaction

from apps.productos import models
from apps.tiendas import models as tiendaModels
from apps.productos.models import Producto
from apps.inventarios.serializers.registrar_inventario_serializer import InventarioRegistrarSerializer
from apps.productos.serializers.producto_serializer import ProductoSerializer
from apps.productos.serializers.registrar_producto_serializer import ProductoRegistrarSerializer
from apps.productos.serializers.actualizar_producto_serializer import ProductoActualizarSerializer
from core.assets.permissions.user_permission import EstaAutenticadoPermission, SuperUsuarioPermission
from core.assets.reutilizable.funciones_reutilizables import respuestaJson
from core.assets.validations.obtener_error_serializer import *
from core.settings.base import SUCCESS_MESSAGE, BD_ERROR_MESSAGE


class ProductoView(GenericViewSet):

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

    def list(self, request):
        try:
            if request.user.is_superuser:
                queryset = models.Producto.objects.all().order_by('-prod_estado','prod_descripcion')
                productos_serializer = ProductoSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, productos_serializer.data, True)
            else:
                queryset = models.Producto.objects.filter(prod_estado=True)
                productos_serializer = ProductoSerializer(queryset, many=True)
                return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, productos_serializer.data, True)
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def create(self, request):
        try:
            registrar_producto_serializer = ProductoRegistrarSerializer(data=request.data)
            if registrar_producto_serializer.is_valid():
                if float(registrar_producto_serializer.data.get('prod_precio_compra')) >= float(registrar_producto_serializer.data.get('prod_precio_venta')):
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                         message="El precio de compra no puede ser mayor o igual al precio de venta.")

                with transaction.atomic():
                    registrar_producto_serializer.create(request.data)
                    last_product = Producto.objects.latest('prod_id')
                    product = ProductoSerializer(last_product)

                    tiendas = tiendaModels.Tienda.objects.all()

                    for tie in tiendas:

                        inventario_agregar = {
                            'producto':product.data.get('prod_id'),
                            'tienda':tie.tie_id,
                            'stock':0
                        }

                        inventario = InventarioRegistrarSerializer(data=inventario_agregar)

                        if not inventario.is_valid():
                            transaction.set_rollback(rollback=True)
                            return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                                 message=obtenerErrorSerializer(inventario))
                        inventario.save()

                    return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, registrar_producto_serializer.data, True)
            else:
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                     message=obtenerErrorSerializer(registrar_producto_serializer))
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def update(self, request, pk=None):
        try:
            prod_id_buscado = self.kwargs['pk']
            if validarEsNumerico(prod_id_buscado) and validarEsMayorQueCero(prod_id_buscado):
                producto_obtenido = Producto.objects.get(prod_id=prod_id_buscado)
                if request.data.get('prod_id') == int(prod_id_buscado):
                    producto_serializer = ProductoActualizarSerializer(producto_obtenido, data=request.data)

                    if producto_serializer.is_valid():
                        if producto_serializer.data.get( 'prod_precio_compra') >= producto_serializer.data.get('prod_precio_venta'):
                            return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                                 message="El precio de compra no puede ser mayor o igual al precio de venta.")

                        producto_serializer.update(producto_obtenido, request.data)
                        return respuestaJson(status.HTTP_200_OK, SUCCESS_MESSAGE, producto_serializer.data, True)
                    else:
                        return respuestaJson(code=status.HTTP_400_BAD_REQUEST,
                                             message=obtenerErrorSerializer(producto_serializer))
                else:
                    mensaje = 'Los parámetros y el ID enviado deben coincidir'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST,message=mensaje)

        except Producto.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="El producto no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=BD_ERROR_MESSAGE)

    def destroy(self, request, pk=None):
        try:
            prod_id_obtenido = self.kwargs['pk']
            if validarEsNumerico(prod_id_obtenido) and validarEsMayorQueCero(prod_id_obtenido):
                producto_obtenido = Producto.objects.get(prod_id=prod_id_obtenido)
                producto_actualizado = ProductoSerializer(producto_obtenido)
                filas_modificadas = Producto.objects.filter(prod_id=prod_id_obtenido).update(
                    prod_estado= not producto_actualizado.data.get('prod_estado')
                )
                if filas_modificadas == 1:
                    return respuestaJson(status.HTTP_200_OK,SUCCESS_MESSAGE,success=True)
                else:
                    mensaje = 'El producto no existe o nose ha podido desactivar/activar'
                    return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)
            else:
                mensaje = 'Los parámetros deben ser numéricos y mayores a 0.'
                return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message=mensaje)

        except Producto.DoesNotExist:
            return respuestaJson(code=status.HTTP_400_BAD_REQUEST, message="El producto no existe.")
        except DatabaseError:
            return respuestaJson(code=status.HTTP_500_INTERNAL_SERVER_ERROR,message=BD_ERROR_MESSAGE)