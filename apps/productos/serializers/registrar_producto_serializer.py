from rest_framework.serializers import Serializer

from rest_framework import serializers
from apps.productos.models import Producto
from apps.proveedores.models import Proveedor
from apps.tallas.models import Talla
from apps.categorias.models import Categoria
from apps.marcas.models import Marca
from apps.modelos.models import Modelo
from apps.colores.models import Color

from core.assets.validations.obtener_error_serializer import validarCaracteresAlfaNumericos

from core.assets.validations.obtener_error_serializer import validarEsNumerico,validarCaracteresAlfanumericosGuiones


class ProductoRegistrarSerializer(Serializer):
    prod_codigo = serializers.CharField(required=True,allow_blank=True,
                                        error_messages={"required": "El código del producto es requerido.",
                                                        "blank": "El código del producto no debe estar vacío",
                                                        "invalid": "El código del producto debe ser válido.",
                                                        })
    prod_descripcion = serializers.CharField(required=True,
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
    prod_precio_venta_base = serializers.DecimalField(max_digits=5, decimal_places=2, required=True,
                                                      error_messages={
                                                          "required": "El precio de venta base del producto es "
                                                                      "requerido.",
                                                          "blank": "El precio de venta base del producto no debe "
                                                                   "estar vacío",
                                                          "invalid": "El precio de venta base del producto debe ser "
                                                                     "válido.",
                                                      })
    prod_precio_venta = serializers.DecimalField(max_digits=5, decimal_places=2, required=True,
                                                 error_messages={
                                                     "required": "El precio de venta del producto es "
                                                                 "requerido.",
                                                     "blank": "El precio de venta del producto no debe "
                                                              "estar vacío",
                                                     "invalid": "El precio de venta del producto debe ser "
                                                                "válido.",
                                                 })
    prod_descuento_promocion = serializers.DecimalField(max_digits=5, decimal_places=2, required=True,
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

    def validate_prod_codigo(self, value):
        if len(value) == 0 :
            return value
        if len(value) == 6:
            if validarCaracteresAlfanumericosGuiones(value):
                prod_codigo = Producto.objects.filter(prod_codigo=value)
                if not prod_codigo.exists():
                    return value
                else:
                    raise serializers.ValidationError("El código del producto ingresado ya existe.")
            else:
                raise serializers.ValidationError("El código del producto puede contener caracteres alfanuméricos y guiones.")
        else:
            raise serializers.ValidationError("El código del producto debe tener 6 caracteres.")

    def validate_prod_descripcion(self,value):

        if len(str.strip(value))>= 5:
            if len(value) <= 50:
                if validarCaracteresAlfaNumericos(value):
                    prod_descripcion = Producto.objects.filter(prod_descripcion=value)
                    if not prod_descripcion.exists():
                        return value
                    else:
                        raise serializers.ValidationError("La descripción del producto ingresada ya existe.")
                else:
                    raise serializers.ValidationError("La descripción del producto solo acepta caracteres alfabéticos y espacios.")
            else:
                raise serializers.ValidationError("La descripción del producto no debe tener más de 50 caracteres.")
        else:
            raise serializers.ValidationError("La descripción del producto no debe tener menos de 5 caracteres.")

    def validate_prod_precio_compra_base(self,value):

        if not value <= 0:
            return value
        else:
            raise serializers.ValidationError("El precio de compra base no puede ser 0 o menor que 0.")

    def validate_prod_precio_compra(self, value):

        if not value <= 0:
            return value
        else:
            raise serializers.ValidationError("El precio de compra no puede ser 0 o menor que 0.")

    def validate_prod_precio_venta_base(self, value):

        if not value <= 0:
            return value
        else:
            raise serializers.ValidationError("El precio de venta base no puede ser 0 o menor que 0.")

    def validate_prod_descuento_promocion(self, value):

            if not value <= 0:
                return value
            else:
                raise serializers.ValidationError("El valor del descuento no puede ser 0 o menor que 0.")

    def validate_prod_precio_venta(self, value):

        if not value <= 0:
            return value
        else:
            raise serializers.ValidationError("El precio de venta no puede ser 0 o menor que 0.")

    def validate_proveedor(self,value):

        if validarEsNumerico(value):
            id_proveedor = Proveedor.objects.filter(pro_id=value)
            if id_proveedor.exists():
                return value
            else:
                raise serializers.ValidationError("El id del proveedor ingresado no existe.")
        else:
            raise serializers.ValidationError("El id del proveedor tiene que ser un número.")

    def validate_talla(self, value):

        if validarEsNumerico(value):
            id_talla = Talla.objects.filter(tal_id=value)
            if id_talla.exists():
                return value
            else:
                raise serializers.ValidationError("El id de la talla ingresada no existe.")
        else:
            raise serializers.ValidationError("El id de la talla tiene que ser un número.")

    def validate_categoria(self, value):

        if validarEsNumerico(value):
            id_categoria = Categoria.objects.filter(cat_id=value)
            if id_categoria.exists():
                return value
            else:
                raise serializers.ValidationError("El id de la categoría ingresada no existe.")
        else:
            raise serializers.ValidationError("El id de la categoría tiene que ser un número.")

    def validate_marca(self, value):

        if validarEsNumerico(value):
            id_marca = Marca.objects.filter(mar_id=value)
            if id_marca.exists():
                return value
            else:
                raise serializers.ValidationError("El id de la marca ingresada no existe.")
        else:
            raise serializers.ValidationError("El id de la marca tiene que ser un número.")

    def validate_modelo(self,value):

        if validarEsNumerico(value):
            id_modelo = Modelo.objects.filter(mod_id=value)
            if id_modelo.exists():
                return value
            else:
                raise serializers.ValidationError("El id del modelo ingresado no existe.")
        else:
            raise serializers.ValidationError("El id del modelo tiene que ser un número.")

    def validate_color(self,value):

        if validarEsNumerico(value):
            id_color = Color.objects.filter(col_id=value)
            if id_color.exists():
                return value
            else:
                raise serializers.ValidationError("El id del color ingresado no existe.")
        else:
            raise serializers.ValidationError("El id del color tiene que ser un número.")

    def validate_prod_estado(self, value):
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado del producto solo puede ser Verdadero o Falso")

    def update(self, instance, validated_data):
        pass

    def create(self, data):

        print(data)
        if data.get('prod_codigo') is not None:
            prod_codigo = str(data['prod_codigo']).upper()
        else:
            prod_codigo = '';
        prod_descripcion = str(data.get('prod_descripcion')).upper()
        prod_precio_compra_base = data.get('prod_precio_compra_base')
        prod_precio_compra = data.get('prod_precio_compra')
        prod_precio_venta_base = data.get('prod_precio_venta_base')
        prod_precio_venta = data.get('prod_precio_venta')
        prod_descuento_promocion = data.get('prod_descuento_promocion')
        proveedor = data.get('proveedor')
        color = data.get('color')
        modelo = data.get('modelo')
        talla = data.get('talla')
        categoria = data.get('categoria')
        marca = data.get('marca')

        producto_nuevoa = Producto(prod_codigo = prod_codigo, prod_descripcion=prod_descripcion,prod_precio_compra_base=prod_precio_compra_base,
                                  prod_precio_compra=prod_precio_compra,prod_precio_venta_base=prod_precio_venta_base,prod_precio_venta=prod_precio_venta,
                                  prod_descuento_promocion=prod_descuento_promocion,proveedor=proveedor,color=color,modelo=modelo,talla=talla,
                                  categoria=categoria,marca=marca,prod_estado=True)
        print(producto_nuevoa)
        producto_nuevoa.save()
