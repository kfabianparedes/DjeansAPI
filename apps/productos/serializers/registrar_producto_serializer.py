from rest_framework.serializers import Serializer

from rest_framework import serializers


class ProductoRegistrarSerializer(Serializer):
    prod_codigo = serializers.CharField(required=False,
                                        error_messages={"required": "El código del producto es requerido.",
                                                        "blank": "El código del producto no debe estar vacío",
                                                        "invalid": "El código del producto debe ser válido.",
                                                        })
    prod_descripcion = serializers.CharField(required=False,
                                             error_messages={"required": "La descripción del producto es requerida.",
                                                             "blank": "La descripción del producto no debe estar vacía",
                                                             "invalid": "La descripción del producto debe ser válida.",
                                                             })
    prod_precio_compra_base = serializers.DecimalField(max_digits=5, decimal_places=2, required=True,
                                                       error_messages={
                                                           "required": "El precio de compra base del producto es "
                                                                       "requerido.",
                                                           "blank": "El precio de compra base del producto no debe "
                                                                    "estar vacía",
                                                           "invalid": "El precio de compra base del producto debe ser "
                                                                      "válida.",
                                                       })
    prod_precio_compra = serializers.DecimalField(max_digits=5, decimal_places=2, required=True,
                                                  error_messages={
                                                      "required": "El precio de compra del producto es requerido.",
                                                      "blank": "El precio de compra del producto no debe estar vacío",
                                                      "invalid": "El precio de compra del producto debe ser válido.",
                                                  })
    prod_precio_venta_base = serializers.DecimalField(max_digits=5, decimal_places=2, required=False,
                                                      error_messages={
                                                          "required": "El precio de venta base del producto es "
                                                                      "requerido.",
                                                          "blank": "El precio de venta base del producto no debe "
                                                                   "estar vacío",
                                                          "invalid": "El precio de venta base del producto debe ser "
                                                                     "válido.",
                                                      })
    prod_precio_venta = serializers.DecimalField(max_digits=5, decimal_places=2, required=False,
                                                 error_messages={
                                                     "required": "El precio de venta del producto es "
                                                                 "requerido.",
                                                     "blank": "El precio de venta del producto no debe "
                                                              "estar vacío",
                                                     "invalid": "El precio de venta del producto debe ser "
                                                                "válido.",
                                                 })
    prod_promocion = serializers.DecimalField(max_digits=5, decimal_places=2, required=False,
                                              error_messages={
                                                  "required": "El descuento de promoción del producto es requerido.",
                                                  "blank": "El descuento de promoción del producto no debe estar vacío",
                                                  "invalid": "El descuento de promoción del producto debe ser válido.",
                                              })

    proveedor = serializers.IntegerField(required=True,
                                         error_messages={
                                             'required': 'El proveedor es requerido',
                                             'null': 'El proveedor no debe ser estar vacío.',
                                             'invalid': 'El proveedor debe ser un número entero.',
                                         })

    categoria = serializers.IntegerField(required=True,
                                         error_messages={
                                             'required': 'La categoría es requerida',
                                             'null': 'La categoría no debe ser estar vacía.',
                                             'invalid': 'La categoría debe ser un número entero.',
                                         })
    marca = serializers.IntegerField(required=True,
                                     error_messages={
                                         'required': 'La marca es requerida',
                                         'null': 'La marca no debe ser estar vacía.',
                                         'invalid': 'La marca debe ser un número entero.',
                                     })
    modelo = serializers.IntegerField(required=True,
                                      error_messages={
                                          'required': 'El modelo es requerido',
                                          'null': 'El modelo no debe ser estar vacío.',
                                          'invalid': 'El modelo debe ser un número entero.',
                                      })
    color = serializers.IntegerField(required=True,
                                     error_messages={
                                         'required': 'El color es requerido',
                                         'null': 'El color no debe ser estar vacío.',
                                         'invalid': 'El color debe ser un número entero.',
                                     })
    talla = serializers.IntegerField(required=True,
                                     error_messages={
                                         'required': 'La talla es requerida',
                                         'null': 'La talla no debe ser estar vacía.',
                                         'invalid': 'La talla debe ser un número entero.',
                                     })
    prod_estado = serializers.BooleanField(required=True,
                                           error_messages={"required": "El estado del producto es requerido.",
                                                           "blank": "El estado del producto no debe estar vacío",
                                                           "invalid": "El estado del producto debe ser válido.",
                                                           })

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
