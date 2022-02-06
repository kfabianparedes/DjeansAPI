from django.db import models

# Create your models here.
class Categoria(models.Model):
    CAT_ID = models.BigAutoField(primary_key=True, unique=True)
    CAT_DESCRIPCION = models.CharField(max_length=50)
    CAT_ESTADO = models.BooleanField(default=True)

    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def _str_(self):
        return self.cat_descripcion