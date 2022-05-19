from rest_framework.serializers import Serializer

from rest_framework import serializers

from apps.compras.models import Compra
from apps.productos.models import Producto
from apps.proveedores.models import Proveedor
from apps.usuarios.models import Usuario

from core.assets.validations.obtener_error_serializer import validarEsNumerico, validarCaracteresAlfanumericosGuiones


class CompraRegistrarSerializer(Serializer):
    comp_monto_total = serializers.DecimalField(max_digits=5, decimal_places=2,
                                                error_messages={
                                                    "required": "El monto de compra es requerido.",
                                                    "blank": "El monto de compra no debe estar vacío",
                                                    "invalid": "El monto de compra debe ser válido.",
                                                })
    usuario = serializers.IntegerField(required=True,
                                       error_messages={
                                           'required': 'El usuario es requerido',
                                           'null': 'El usuario no debe ser estar vacío.',
                                           'invalid': 'El usuario debe ser un número entero.',
                                       })
    proveedor = serializers.IntegerField(required=True,
                                         error_messages={
                                             'required': 'El proveedor es requerido',
                                             'null': 'El proveedor no debe ser estar vacío.',
                                             'invalid': 'El proveedor debe ser un número entero.',
                                         })

    def validate_comp_monto_total(self, value):
        if not value <= 0:
            return value
        else:
            raise serializers.ValidationError("El monto total de compra no puede ser 0 o menor que 0.")

    def validate_usuario(self, value):
        if validarEsNumerico(value):
            usuario = Usuario.objects.filter(id=value)
            if usuario.exists():
                return value
            else:
                raise serializers.ValidationError("El identificador de usuario ingresado no existe.")
        else:
            raise serializers.ValidationError("El identificador de usuario tiene que ser numérico.")

    def validate_proveedor(self, value):
        if validarEsNumerico(value):
            proveedor = Proveedor.objects.filter(pro_id=value)
            if proveedor.exists():
                return value
            else:
                raise serializers.ValidationError("El identificador del proveedor ingresado no existe.")
        else:
            raise serializers.ValidationError("El identificador del proveedor tiene que ser numérico.")

    def save(self, **kwargs):
        comp_monto_total = self.data.get('comp_monto_total')
        usuario = self.data.get('usuario')
        proveedor = self.data.get('proveedor')
        compra = Compra(comp_monto_total=comp_monto_total, usuario=usuario, proveedor=proveedor)
        compra.save()
