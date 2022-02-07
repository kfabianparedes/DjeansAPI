from django.db import models
from apps.sucursales.models import SUCURSALES

# Create your models here.
class TIENDAS(models.Model):
    TIE_ID=models.AutoField(primary_key=True,verbose_name='TIE_ID')
    TIE_NOMBRE=models.CharField(max_length=50)
    TIE_ESTADO=models.BooleanField(default=True)
    TIE_SUC_ID=models.ForeignKey(SUCURSALES,on_delete=models.CASCADE,verbose_name='TIE_SUC_ID')
    class Meta:
        ordering=["TIE_ID"]
        db_table='tienda'
