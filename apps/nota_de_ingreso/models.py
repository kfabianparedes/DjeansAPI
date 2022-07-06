from django.db import models
from django.utils import timezone

from apps.compras.models import Compra
from apps.tiendas.models import Tienda


class NotaDeIngreso(models.Model):
    nota_ingreso_id = models.AutoField(primary_key=True)
    tienda = models.ForeignKey(Tienda, related_name='tienda', on_delete=models.PROTECT)
    compra = models.ForeignKey(Compra, related_name='compra', on_delete=models.PROTECT)
    nota_ingreso_registro = models.DateField("Fecha registro", default=timezone.now)

    class Meta:
        db_table = 'nota_de_ingreso'
        verbose_name = 'Nota de Ingreso'
        verbose_name_plural = 'Notas de Ingreso'

    def _str_(self):
        return self.nota_ingreso_registro
