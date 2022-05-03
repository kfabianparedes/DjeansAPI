from django.db import models


class Proveedor(models.Model):
    pro_id = models.AutoField(primary_key=True, verbose_name='pro_id')
    pro_ruc = models.CharField(max_length=11)
    pro_razon_social = models.CharField(max_length=50)
    pro_nombre = models.CharField(max_length=50)
    pro_email = models.EmailField(max_length=50)
    pro_telefono1 = models.CharField(max_length=12)
    pro_telefono2 = models.CharField(max_length=12)
    pro_direccion1 = models.CharField(max_length=50)
    pro_direccion2 = models.CharField(max_length=50)
    pro_estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def _str_(self):
        return self.pro_nombre
