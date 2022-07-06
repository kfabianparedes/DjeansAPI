from django.db import models

from apps.compras.models import Compra


class GuiaDeRemision(models.Model):
    guia_id = models.AutoField(primary_key=True)
    guia_serie = models.CharField(verbose_name='Nro. serie', max_length=4)
    guia_numero = models.CharField(verbose_name='Nro. guía', max_length=8)
    guia_fecha = models.DateField(verbose_name='Fecha guía remisión')
    # guia_flete = models.DecimalField(verbose_name='Flete', max_digits=5, decimal_places=2)
    compra = models.ForeignKey(Compra, related_name='guia_compra', on_delete=models.CASCADE)

    class Meta:
        db_table = 'guia_de_remision'
        verbose_name = 'Guía de remisión'
        verbose_name_plural = 'Guías de remisión'

    def _str_(self):
        return f'Guía de remisión : {self.guia_serie}-{self.guia_numero}'




