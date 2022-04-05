from django.db import models


class Modelo(models.Model):
    mod_id = models.BigAutoField(primary_key=True, unique=True)
    mod_descripcion = models.CharField(max_length=50)
    mod_estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'modelo'
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def _str_(self):
        return self.mod_descripcion
