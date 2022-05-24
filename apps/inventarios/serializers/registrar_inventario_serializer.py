from rest_framework.serializers import Serializer

from rest_framework import serializers
from apps.inventarios.models import Inventario
from apps.productos.models import Producto
from apps.tiendas.models import Tienda

from core.assets.validations.obtener_error_serializer import validarEsNumerico

class InventarioRegistrarSerializer(Serializer):
    producto = serializers.IntegerField(required=True,
                                        error_messages={
                                            'required': 'El identificador del producto es requerido',
                                            'null': 'El identificador del producto no debe ser estar vacío.',
                                            'invalid': 'El identificador del producto debe ser un número entero.',
                                        })
    tienda = serializers.IntegerField(required=True,
                                        error_messages={
                                            'required': 'El identificador de tienda es requerido',
                                            'null': 'El identificador de tienda no debe ser estar vacío.',
                                            'invalid': 'El identificador de tienda debe ser un número entero.',
                                        })
    stock = serializers.IntegerField(required=True,
                                        error_messages={
                                            'required': 'El stock es requerido',
                                            'null': 'El stock no debe ser estar vacío.',
                                            'invalid': 'El stock debe ser un número entero.',
                                        })

    def validate_stock(self, value):
        if validarEsNumerico(value):
            if value >= 0:
                return value
            else:
                raise serializers.ValidationError("El stock no puede ser menos que 0.")
        else:
            raise serializers.ValidationError("El stock tiene que ser numérico.")

    def validate_producto(self, value):
        if validarEsNumerico(value):
            producto = Producto.objects.filter(prod_id=value)
            if producto.exists():
                return value
            else:
                raise serializers.ValidationError("El identificador del producto ingresado no existe.")
        else:
            raise serializers.ValidationError("El identificador del producto tiene que ser numérico.")

    def validate_tienda(self, value):
        if validarEsNumerico(value):
            tienda = Tienda.objects.filter(tie_id=value)
            if tienda.exists():
                return value
            else:
                raise serializers.ValidationError("El indentificador de la tienda ingresado no existe.")
        else:
            raise serializers.ValidationError("El identificador de la tienda tiene que ser numérico.")

    def save(self, **kwargs):

        producto = self.data.get('producto')
        tienda = self.data.get('tienda')
        stock = self.data.get('stock')

        inventario_nuevo = Inventario(
            producto=producto,
            tienda=tienda,
            stock=stock
        )

        inventario_nuevo.save()
