from django.db import models

# Create your models here.
class PROVEEDORES(models.Model):
    PRO_ID=models.AutoField(primary_key=True,verbose_name='PRO_ID')
    PRO_RUC=models.CharField(max_length=11)
    PRO_NOMBRE=models.CharField(max_length=50)
    PRO_EMAIL=models.EmailField(max_length=50)
    SUC_TELEFONO1=models.CharField(max_length=12)
    SUC_TELEFONO2=models.CharField(max_length=12)
    SUC_DIRECCION1=models.CharField(max_length=50)
    SUC_DIRECCION2=models.CharField(max_length=50)
    SUC_ESTADO=models.BooleanField(default=True)
    class Meta:
        ordering=["PRO_ID"]
        db_table='proveedor'