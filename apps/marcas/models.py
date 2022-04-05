from django.db import models


class Marca(models.Model):
    mar_id = models.AutoField(primary_key=True, unique=True)
    mar_descripcion = models.CharField(max_length=30)
    mar_estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'marca'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def _str_(self):
        return self.mar_descripcion
