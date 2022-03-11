from django.db import models


class TipoDeDocumento(models.Model):
    tipo_doc_id = models.BigAutoField(verbose_name='Tipo de documento - ID', primary_key=True)
    tipo_doc_descripcion = models.CharField(verbose_name='Descripción', max_length=30, blank=False, null=False)

    class Meta:
        db_table = 'tipo_documento_personal'
        verbose_name = 'Tipo documento personal'
        verbose_name_plural = 'Tipos de documentos personales'

    def __str__(self):
        return f'{self.tipo_doc_descripcion}'
