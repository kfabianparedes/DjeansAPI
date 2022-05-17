from django.db import models


class Producto(models.Model):
    prod_id = models.AutoField(primary_key=True, verbose_name='ID')
    prod_codigo = models.CharField(verbose_name='Código', unique=True, blank=True, max_length = 10)
    prod_descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    prod_precio_compra_base = models.DecimalField(verbose_name='Precio de compra base', max_digits = 5 , decimal_places = 2)
    prod_precio_compra = models.DecimalField(verbose_name='Precio de compra', max_digits = 5 , decimal_places = 2)
    prod_precio_venta_base = models.DecimalField(verbose_name='Precio de venta base', max_digits = 5 , decimal_places = 2)
    prod_precio_venta = models.DecimalField(verbose_name='Precio de venta', max_digits = 5 , decimal_places = 2)
    prod_promocion = models.DecimalField(verbose_name='Promoción', max_digits = 5 , decimal_places = 2)

    proveedor = models.IntegerField(verbose_name='Proveedor',blank=False,null=False)
    categoria = models.IntegerField(verbose_name='Categoría',blank=False,null=False)
    marca = models.IntegerField(verbose_name='Marca',blank=False,null=False)
    modelo = models.IntegerField(verbose_name='Modelo',blank=False,null=False)
    color = models.IntegerField(verbose_name='Color',blank=False,null=False)
    talla = models.IntegerField(verbose_name='Talla',blank=False,null=False)

    prod_estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def _str_(self):
        return self.prod_descripcion
