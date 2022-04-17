from django.db import models


class Sucursal(models.Model):
    suc_id = models.AutoField(primary_key=True, verbose_name='suc_id')
    suc_nombre = models.CharField(max_length=50)
    suc_direccion = models.CharField(max_length=50)
    suc_estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'sucursal'
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
