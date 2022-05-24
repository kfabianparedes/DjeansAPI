from django.db import models


# Create your models here.

class Inventario(models.Model):
    inv_id = models.AutoField(primary_key=True)
    tienda = models.IntegerField(verbose_name='Tienda',blank=False,null=False)
    producto = models.IntegerField(verbose_name='Producto', blank=False, null=False)
    stock = models.IntegerField(verbose_name='Stock',blank=False,null=False)

    class Meta:
        db_table = 'inventario'
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventario'

    def __str__(self):
        return f'Inventario de la tienda: {(self.tienda)}'
