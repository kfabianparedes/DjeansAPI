from django.db import models
from apps.sucursales.models import SUCURSALES

# Create your models here.
class TIENDAS(models.Model):
    tie_id=models.AutoField(primary_key=True,verbose_name='tie_id')
    tie_nombre=models.CharField(max_length=50)
    tie_estado=models.BooleanField(default=True)
    tie_suc_id=models.ForeignKey(SUCURSALES,on_delete=models.CASCADE,verbose_name='tie_suc_id',related_name="tie_suc_id")
    class Meta:
        ordering=["tie_id"]
        db_table='tienda'
