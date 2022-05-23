from django.db import models

from apps.compras.models import Compra


class DetalleDeCompra(models.Model):
    det_comp_id = models.AutoField(primary_key=True)
    det_comp_cantidad = models.IntegerField(verbose_name='Cantidad')
    det_comp_importe = models.DecimalField(verbose_name='Monto detalle', max_digits=5, decimal_places=2)
    producto = models.IntegerField(verbose_name='Producto')
    compra = models.ForeignKey(Compra, related_name='detalle_compra', on_delete=models.CASCADE)

    class Meta:
        db_table = 'detalle_de_compra'
        verbose_name = 'Detalle de compra'
        verbose_name_plural = 'Detalles de compra'

    def _str_(self):
        return f'Monto total : {(self.det_comp_importe * self.det_comp_cantidad)}'
