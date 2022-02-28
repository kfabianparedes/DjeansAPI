from django.db import models

# Create your models here.
class COLOR(models.Model):
    COL_ID = models.BigAutoField(primary_key=True, unique=True)
    COL_DESCRIPCION = models.CharField(max_length=50)
    COL_ESTADO = models.BooleanField(default=True)

    class Meta:
        db_table = 'color'
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'

    def _str_(self):
        return self.COL_DESCRIPCION