from mmap import PAGESIZE
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
# def validate_geeks_mail(value):
#     if "@gmail.com" in value:
#         return value
#     else:
#         raise ValidationError("This field accepts mail id of google only")
class SUCURSALES(models.Model):
    SUC_ID=models.AutoField(primary_key=True,verbose_name='SUC_ID')
    SUC_NOMBRE=models.CharField(max_length=50)
    # SUC_DIRECCION=models.CharField(max_length=50,validators=[validate_geeks_mail])
    SUC_DIRECCION=models.CharField(max_length=50)
    SUC_ESTADO=models.BooleanField(default=True)
    class Meta:
        ordering=["SUC_ID"]
        db_table='sucursal'
        