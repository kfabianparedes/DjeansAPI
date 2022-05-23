from rest_framework.serializers import Serializer

from rest_framework import serializers
from apps.compras.models import Compra
from apps.detalles_de_compra.models import DetalleDeCompra
from apps.productos.models import Producto

from core.assets.validations.obtener_error_serializer import validarEsNumerico


class DetalleDeCompraRegistrarSerializer(Serializer):
    det_comp_cantidad = serializers.IntegerField(required=True,
                                                 error_messages={
                                                     'required': 'La cantidad del producto en el detalle es requerida',
                                                     'null': 'La cantidad del producto en el detalle no debe ser '
                                                             'estar vacía.',
                                                     'invalid': 'La cantidad del producto en el detalle debe ser un '
                                                                'número entero.',
                                                 })
    det_comp_importe = serializers.DecimalField(max_digits=5, decimal_places=2,
                                                error_messages={
                                                    "required": "El monto del detalle es requerido.",
                                                    "blank": "El monto del detalle no debe estar vacío",
                                                    "invalid": "El monto del detalle debe ser válido.",
                                                })
    producto = serializers.IntegerField(required=True,
                                        error_messages={
                                            'required': 'El identificador del producto es requerido',
                                            'null': 'El identificador del producto no debe ser estar vacío.',
                                            'invalid': 'El identificador del producto debe ser un número entero.',
                                        })
    compra = serializers.IntegerField(required=True,
                                      error_messages={
                                          'required': 'El identificador de la compra es requerido',
                                          'null': 'El identificador de la compra no debe ser estar vacío.',
                                          'invalid': 'El identificador de la compra debe ser un número entero.',
                                      })

    def validate_det_comp_cantidad(self, value):
        if not value <= 0:
            return value
        else:
            raise serializers.ValidationError("La cantidad de productos debe ser mayor a 0.")

    def validate_det_comp_importe(self, value):
        if not value <= 0:
            return value
        else:
            raise serializers.ValidationError("El monto total del detalle debe ser mayor a 0.")

    def validate_producto(self, value):
        if validarEsNumerico(value):
            producto = Producto.objects.filter(prod_id=value)
            if producto.exists():
                return value
            else:
                raise serializers.ValidationError("El identificador del producto ingresado no existe.")
        else:
            raise serializers.ValidationError("El identificador del producto tiene que ser numérico.")

    def validate_compra(self, value):
        if validarEsNumerico(value):
            compra = Compra.objects.filter(comp_id=value)
            if compra.exists():
                return value
            else:
                raise serializers.ValidationError("El identificador de la compra no existe.")
        else:
            raise serializers.ValidationError("El identificador de la compra tiene que ser numérico.")

    def save(self, **kwargs):
        det_comp_cantidad = self.data.get('det_comp_cantidad')
        det_comp_importe = self.data.get('det_comp_importe')
        producto = self.data.get('producto')
        compra_nueva = Compra()
        compra_nueva.comp_id = self.data.get('compra')
        compra = compra_nueva
        detalle_de_compra = DetalleDeCompra(
            det_comp_cantidad=det_comp_cantidad,
            det_comp_importe=det_comp_importe,
            producto=producto,
            compra=compra
        )
        detalle_de_compra.save()
