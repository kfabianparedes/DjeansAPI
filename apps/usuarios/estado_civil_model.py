from django.db import models


class EstadoCivil(models.Model):
    est_civil_id = models.BigAutoField(verbose_name='Estado Civil ID', primary_key=True)
    est_civil_descripcion = models.CharField(verbose_name='Descripción', max_length=30, blank=False, null=False)

    class Meta:
        db_table = 'estado_civil'
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civiles'

    def __str__(self):
        return self.est_civil_descripcion

