from rest_framework.serializers import Serializer

from rest_framework import serializers

from apps.compras.models import Compra
from apps.proveedores.models import Proveedor
from apps.tipo_comprobante.models import TipoComprobante
from apps.usuarios.models import Usuario

from core.assets.validations.obtener_error_serializer import validarEsNumerico, validarNumeroSerie


class CompraRegistrarSerializer(Serializer):
    comp_importe_total = serializers.DecimalField(max_digits=5, decimal_places=2,
                                                  error_messages={
                                                      "required": "El monto de compra es requerido.",
                                                      "blank": "El monto de compra no debe estar vacío",
                                                      "invalid": "El monto de compra debe ser válido.",
                                                  })
    comp_fecha_emision = serializers.DateField(error_messages={
                                                   "required": "La fecha de emisión de la compra es requerida.",
                                                   "blank": "La fecha de emisión de la compra no debe estar vacía",
                                                   "invalid": "La fecha de emisión de la compra debe ser válida. "
                                                              "YYYY-MM-DD",
                                               })
    comp_serie = serializers.CharField(required=True,
                                       error_messages={
                                           'required': 'La serie de la compra es requerida',
                                           'null': 'La serie de la compra no debe estar vacía.',
                                           'invalid': 'La serie de la compra debe ser numérica.',
                                       })
    comp_numero = serializers.CharField(required=True,
                                        error_messages={
                                            'required': 'El número de compra es requerido',
                                            'null': 'El número de compra no debe estar vacío.',
                                            'invalid': 'El número de compra debe ser numérico.',
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
    tipo_comprobante = serializers.IntegerField(required=True,
                                                error_messages={
                                                    'required': 'El tipo de comprobante es requerido',
                                                    'null': 'El tipo de comprobante no debe ser estar vacío.',
                                                    'invalid': 'El tipo de comprobante debe ser un número entero.',
                                                })

    def validate_comp_importe_total(self, value):
        if not value <= 0:
            return value
        else:
            raise serializers.ValidationError("El monto total de compra no puede ser 0 o menor que 0.")

    def validate_comp_serie(self, value):
        if validarNumeroSerie(value):
            if len(str.strip(value)) == 4:
                print(len(value))
                return value
            raise serializers.ValidationError("La cantidad de caracteres del número de serie debe ser 4.")
        else:
            raise serializers.ValidationError("El número serie del comprobante de compra tiene que empezar con B o F "
                                              "seguido de 3 dígitos numéricos.")

    def validate_comp_numero(self, value):
        if validarEsNumerico(value):
            if 4 <= len(str.strip(value)) <= 8:
                return value
            raise serializers.ValidationError("La cantidad de caracteres del número de comprobante debe tener entre 4 "
                                              "y 8 dígitos.")
        else:
            raise serializers.ValidationError("El número del comprobante de compra tiene que ser numérico.")

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

    def validate_tipo_comprobante(self, value):
        if validarEsNumerico(value):
            comprobante = TipoComprobante.objects.filter(tipo_comprobante_id=value)
            if comprobante.exists():
                return value
            else:
                raise serializers.ValidationError("El identificador del tipo de comprobante ingresado no existe.")
        else:
            raise serializers.ValidationError("El identificador del tipo de comprobante tiene que ser numérico.")

    def save(self, **kwargs):
        comp_importe_total = self.data.get('comp_importe_total')
        comp_fecha_emision = self.data.get('comp_fecha_emision')
        comp_serie = self.data.get('comp_serie')
        comp_numero = self.data.get('comp_numero')
        usuario = self.data.get('usuario')
        proveedor = self.data.get('proveedor')
        comprobante = TipoComprobante()
        comprobante.tipo_comprobante_id = self.data.get('tipo_comprobante')

        compra = Compra(
            comp_importe_total=comp_importe_total,
            comp_fecha_emision=comp_fecha_emision,
            comp_serie=comp_serie,
            comp_numero=comp_numero,
            usuario=usuario,
            proveedor=proveedor,
            tipo_comprobante=comprobante
        )
        compra.save()
