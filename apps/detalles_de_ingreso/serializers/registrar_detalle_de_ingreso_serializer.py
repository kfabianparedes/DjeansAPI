from rest_framework.serializers import Serializer
from rest_framework import serializers

from apps.compras.models import Compra
from apps.detalles_de_ingreso.models import DetalleDeIngreso
from apps.nota_de_ingreso.models import NotaDeIngreso
from apps.productos.models import Producto
from core.assets.validations.obtener_error_serializer import validarEsNumerico


class DetalleDeIngresoRegistrarSerializer(Serializer):
    det_ingreso_cantidad = serializers.IntegerField(required=True,
                                                    error_messages={
                                                        'required': 'La cantidad del producto en el detalle es '
                                                                    'requerida',
                                                        'null': 'La cantidad del producto en el detalle no debe ser '
                                                                'estar vacía.',
                                                        'invalid': 'La cantidad del producto en el detalle debe ser un '
                                                                   'número entero.',
                                                    })

    producto = serializers.IntegerField(required=True,
                                        error_messages={
                                            'required': 'El identificador del producto es requerido',
                                            'null': 'El identificador del producto no debe ser estar vacío.',
                                            'invalid': 'El identificador del producto debe ser un número entero.',
                                        })

    nota_de_ingreso = serializers.IntegerField(required=True,
                                               error_messages={
                                                   'required': 'El identificador de la Nota de Ingreso es requerido',
                                                   'null': 'El identificador de la Nota de Ingreso no debe ser estar '
                                                           'vacío.',
                                                   'invalid': 'El identificador de la Nota de Ingreso debe ser un número '
                                                              'entero.',
                                               })

    def validate_producto(self, value):
        if validarEsNumerico(value):
            producto = Producto.objects.filter(prod_id=value)
            if producto.exists():
                return value
            else:
                raise serializers.ValidationError("El identificador del producto ingresado no existe.")
        else:
            raise serializers.ValidationError("El identificador del producto tiene que ser numérico.")

    def validate_nota_de_ingreso(self, value):
        if validarEsNumerico(value):
            compra = NotaDeIngreso.objects.filter(nota_ingreso_id=value)
            if compra.exists():
                return value
            else:
                raise serializers.ValidationError("El identificador del la Nota de Ingreso ingresado no existe.")
        else:
            raise serializers.ValidationError("El identificador del la Nota de Ingreso tiene que ser numérico.")

    def save(self):
        nota_ingreso = NotaDeIngreso()
        nota_ingreso.nota_ingreso_id = self.data.get('nota_de_ingreso')
        producto = Producto()
        producto.prod_id = self.data.get('producto')
        det_ingreso_cantidad = self.data.get('det_ingreso_cantidad')
        detalle_ingreso = DetalleDeIngreso(
            det_ingreso_cantidad=det_ingreso_cantidad,
            producto=producto,
            nota_de_ingreso=nota_ingreso
        )
        detalle_ingreso.save()
