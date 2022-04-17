from django.db import models


class Tienda(models.Model):
    tie_id = models.AutoField(primary_key=True)
    tie_nombre = models.CharField(max_length=50)
    tie_estado = models.BooleanField(default=True)
    sucursal = models.IntegerField(verbose_name='Sucursal', blank=False, null=False)

    class Meta:
        db_table = 'tienda'
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'

    def _str_(self):
        return self.tie_nombre

