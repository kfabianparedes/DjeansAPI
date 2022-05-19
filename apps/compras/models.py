from django.db import models
from django.utils import timezone


class Compra(models.Model):
    comp_id = models.AutoField(primary_key=True)
    comp_monto_total = models.DecimalField(verbose_name='Monto total', max_digits=5, decimal_places=2)
    comp_fecha_registro = models.DateTimeField("Fecha registro", default=timezone.now)
    usuario = models.IntegerField(verbose_name='Usuario')
    proveedor = models.IntegerField(verbose_name='Proveedor')

    class Meta:
        db_table = 'compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def _str_(self):
        return self.comp_fecha_registro
