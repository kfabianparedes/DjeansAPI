from django.db import models


class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_tipo = models.CharField(max_length=30, unique=True, blank=False)

    class Meta:
        db_table = 'rol'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def _str_(self):
        return self.rol_tipo

