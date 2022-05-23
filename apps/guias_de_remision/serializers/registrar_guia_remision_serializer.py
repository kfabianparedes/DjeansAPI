from abc import ABC
from rest_framework.serializers import Serializer
from rest_framework import serializers
from apps.compras.models import Compra
from apps.guias_de_remision.models import GuiaDeRemision
from core.assets.validations.obtener_error_serializer import validarEsNumerico


class GuiaDeRemisionRegistrarSerializer(Serializer):
    guia_serie = serializers.CharField(required=True,
                                       error_messages={
                                           'required': 'La serie de la guía de remisión es requerida',
                                           'blank': 'La serie de la guía de remisión no debe estar vacía.',
                                           'invalid': 'La serie de la guía de remisión debe ser numérica.',
                                       })
    guia_numero = serializers.CharField(required=True,
                                        error_messages={
                                            'required': 'El número de guía de remisión es requerido',
                                            'blank': 'El número de guía de remisión no debe estar vacío.',
                                            'invalid': 'El número de guía de remisión debe ser numérico.',
                                        })
    guia_flete = serializers.DecimalField(max_digits=5, decimal_places=2,
                                          error_messages={
                                              "required": "El monto del flete es requerido.",
                                              "blank": "El monto del flete no debe estar vacío",
                                              "invalid": "El monto del flete debe ser válido.",
                                          })
    guia_fecha = serializers.DateField(error_messages={
                                            "required": "La fecha de emisión de la guía es requerida.",
                                            "blank": "La fecha de emisión de la guía no debe estar vacía",
                                            "invalid": "La fecha de emisión de la guía debe ser válida. YYYY-MM-DD",
                                            })
    compra = serializers.IntegerField(required=True,
                                      error_messages={
                                          'required': 'El identificador de la compra es requerido',
                                          'null': 'El identificador de la compra no debe ser estar vacío.',
                                          'invalid': 'El identificador de la compra debe ser un número entero.',
                                      })

    def validate_guia_serie(self, value):
        if validarEsNumerico(value):
            if len(str.strip(value)) == 4:
                return value
            raise serializers.ValidationError("La cantidad de caracteres del número de serie de la guía debe ser 4.")

        else:
            raise serializers.ValidationError("La serie de la guía tiene que ser numérica.")

    def validate_guia_numero(self, value):
        if validarEsNumerico(value):
            if len(str.strip(value)) == 4:
                return value
            raise serializers.ValidationError("La cantidad de caracteres del número de guía debe ser 4.")
        else:
            raise serializers.ValidationError("El número de la guía tiene que ser numérico.")

    def validate_guia_flete(self, value):
        if not value <= 0:
            return value
        else:
            raise serializers.ValidationError("El monto del flete debe ser mayor a 0.")

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
        guia_serie = self.data.get('guia_serie')
        guia_numero = self.data.get('guia_numero')
        guia_fecha = self.data.get('guia_fecha')
        guia_flete = self.data.get('guia_flete')
        compra_nueva = Compra()
        compra_nueva.comp_id = self.data.get('compra')
        compra = compra_nueva
        guia_de_remision = GuiaDeRemision(
            guia_serie=guia_serie,
            guia_numero=guia_numero,
            guia_flete=guia_flete,
            guia_fecha=guia_fecha,
            compra=compra
        )
        guia_de_remision.save()
