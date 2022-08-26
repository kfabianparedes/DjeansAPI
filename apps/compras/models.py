from django.db import models
from django.utils import timezone

from apps.tipo_comprobante.models import TipoComprobante


class Compra(models.Model):
    comp_id = models.AutoField(primary_key=True)
    comp_importe_total = models.DecimalField(verbose_name='Monto total', max_digits=10, decimal_places=2)
    comp_fecha_emision = models.DateField("Fecha emisión")
    comp_fecha_registro = models.DateField("Fecha registro", default=timezone.now)
    comp_serie = models.CharField(verbose_name='Nro. Serie', max_length=8)
    comp_numero = models.CharField(verbose_name='Nro. comprobante', max_length=8)
    comp_ingresada = models.BooleanField(verbose_name='Ingresada a tienda', default=False)
    usuario = models.IntegerField(verbose_name='Usuario')
    proveedor = models.IntegerField(verbose_name='Proveedor')
    tipo_comprobante = models.ForeignKey(TipoComprobante, related_name='tipo_comprobante', on_delete=models.PROTECT)

    class Meta:
        db_table = 'compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def _str_(self):
        return self.comp_fecha_registro
