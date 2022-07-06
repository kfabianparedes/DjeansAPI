from django.db import models

from apps.nota_de_ingreso.models import NotaDeIngreso
from apps.productos.models import Producto


class DetalleDeIngreso(models.Model):
    det_ingreso_id = models.AutoField(primary_key=True)
    det_ingreso_cantidad = models.IntegerField(verbose_name='Cantidad')
    producto = models.ForeignKey(Producto, related_name='producto', on_delete=models.CASCADE)
    nota_de_ingreso = models.ForeignKey(NotaDeIngreso, related_name='nota_de_ingreso', on_delete=models.CASCADE)

    class Meta:
        db_table = 'detalle_de_ingreso'
        verbose_name = 'Detalle de Ingreso'
        verbose_name_plural = 'Detalles de Ingreso'

    def _str_(self):
        return f'{self.det_ingreso_cantidad} de {self.producto}'
