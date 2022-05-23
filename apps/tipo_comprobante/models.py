from django.db import models


class TipoComprobante(models.Model):
    tipo_comprobante_id = models.AutoField(primary_key=True)
    tipo_comprobante_descripcion = models.CharField(verbose_name='Tipo de comprobante', max_length=30)

    class Meta:
        db_table = 'tipo_comprobante'
        verbose_name = 'Tipo de comprobante'
        verbose_name_plural = 'Tipo de comprobante'

    def _str_(self):
        return self.tipo_comprobante_descripcion
