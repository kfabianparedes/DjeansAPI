from django.db import models

# Create your models here.
class MARCAS(models.Model):
    MAR_ID=models.AutoField(primary_key=True,verbose_name='MAR_ID')
    MAR_DESCRIPCION=models.CharField(max_length=50)
    MAR_ESTADO=models.BooleanField(default=True)
    class Meta:
        ordering=["MAR_ID"]
        db_table='marca'