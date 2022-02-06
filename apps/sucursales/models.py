from django.db import models

# Create your models here.
class SUCURSALES(models.Model):
    SUC_ID=models.AutoField(primary_key=True,verbose_name='SUC_ID')
    SUC_NOMBRE=models.CharField(max_length=50)
    SUC_DIRECCION=models.CharField(max_length=50)
    SUC_ESTADO=models.BooleanField(default=True)
    class Meta:
        ordering=["SUC_ID"]
        db_table='sucursal'