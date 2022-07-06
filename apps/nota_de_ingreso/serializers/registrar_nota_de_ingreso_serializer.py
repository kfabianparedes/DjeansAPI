from rest_framework.serializers import Serializer

from rest_framework import serializers

from apps.compras.models import Compra
from apps.nota_de_ingreso.models import NotaDeIngreso
from apps.tiendas.models import Tienda

from core.assets.validations.obtener_error_serializer import validarEsNumerico, validarNumeroSerie


class NotaDeIngresoRegistrarSerializer(Serializer):
    tienda = serializers.IntegerField(required=True,
                                      error_messages={
                                          'required': 'El campo tienda es requerido',
                                          'null': 'El campo tienda no debe ser estar vacío.',
                                          'invalid': 'El campo tienda debe ser un número entero.',
                                      })
    compra = serializers.IntegerField(required=True,
                                      error_messages={
                                          'required': 'El ID de compra es requerido',
                                          'null': 'El ID de compra no debe ser estar vacío.',
                                          'invalid': 'El ID de compra debe ser un número entero.',
                                      })

    def validate_tienda(self, value):
        if validarEsNumerico(value):
            tienda = Tienda.objects.filter(tie_id=value)
            if tienda.exists():
                return value
            else:
                raise serializers.ValidationError("El identificador de la tienda ingresado no existe.")
        else:
            raise serializers.ValidationError("El identificador de la tienda tiene que ser numérico.")

    def validate_compra(self, value):
        if validarEsNumerico(value):
            compra = Compra.objects.filter(comp_id=value)
            if compra.exists():
                return value
            else:
                raise serializers.ValidationError("El identificador del la compra ingresado no existe.")
        else:
            raise serializers.ValidationError("El identificador del la compra tiene que ser numérico.")

    def save(self):
        tienda = Tienda()
        tienda.tie_id = self.data.get('tienda')
        compra = Compra()
        compra.comp_id = self.data.get('compra')

        nota_de_ingreso = NotaDeIngreso(
            tienda=tienda,
            compra=compra
        )
        nota_de_ingreso.save()
