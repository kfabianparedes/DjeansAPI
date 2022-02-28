from django.db import models

# Create your models here.
class MODELO(models.Model):
    MOD_ID = models.BigAutoField(primary_key=True, unique=True)
    MOD_DESCRIPCION = models.CharField(max_length=50)
    MOD_ESTADO = models.BooleanField(default=True)

    class Meta:
        db_table = 'modelo'
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def _str_(self):
        return self.MOD_DESCRIPCION