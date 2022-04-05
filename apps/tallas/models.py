from django.db import models

# Create your models here.
class Talla(models.Model):
    tal_id = models.BigAutoField(primary_key=True, unique=True)
    tal_descripcion = models.CharField(max_length=30)
    tal_estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'talla'
        verbose_name = 'Talla'
        verbose_name_plural = 'Tallas'

    def _str_(self):
        return self.tal_descripcion