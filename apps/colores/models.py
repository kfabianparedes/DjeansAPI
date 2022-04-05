from django.db import models

# Create your models here.


class Color(models.Model):
    col_id = models.BigAutoField(primary_key=True, unique=True)
    col_descripcion = models.CharField(max_length=30)
    col_estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'color'
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'

    def _str_(self):
        return self.col_descripcion