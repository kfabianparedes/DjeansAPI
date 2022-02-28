from django.db import models

# Create your models here.
class TALLA(models.Model):
    TAL_ID = models.BigAutoField(primary_key=True, unique=True)
    TAL_DESCRIPCION = models.CharField(max_length=50)
    TAL_ESTADO = models.BooleanField(default=True)

    class Meta:
        db_table = 'talla'
        verbose_name = 'Talla'
        verbose_name_plural = 'Tallas'

    def _str_(self):
        return self.TAL_DESCRIPCION