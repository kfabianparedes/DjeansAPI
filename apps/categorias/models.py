from django.db import models

# Create your models here.
class Categoria(models.Model):
    cat_id = models.BigAutoField(primary_key=True, unique=True)
    cat_descripcion = models.CharField(max_length=50)
    cat_estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def _str_(self):
        return self.cat_descripcion