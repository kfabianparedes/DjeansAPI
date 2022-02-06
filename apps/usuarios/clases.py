from django.db import models

class EstadoCivil(models.Model):
    ESTADO_CIVIL_ID = models.BigAutoField(verbose_name='Estado Civil ID',primary_key=True)
    ESTADO_CIVIL_DESCRIPCION = models.CharField(verbose_name='Descripción', max_length= 30, blank= False, null= False)

    class Meta:
        db_table = 'estado_civil'
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civiles'

    def __str__(self):
        return self.ESTADO_CIVIL_DESCRIPCION
    
class TipoDocumento(models.Model):
    TIPO_DOC_PER_ID = models.BigAutoField(verbose_name='Tipo de documento - ID',primary_key=True)
    TIPO_DOC_PER_DESCRIPCION = models.CharField(verbose_name='Descripción', max_length= 30, blank= False, null= False)

    class Meta:
        db_table = 'tipo_documento_personal'
        verbose_name = 'Tipo documento personal'
        verbose_name_plural = 'Tipos de documentos personales'

    def __str__(self):
        return f'{self.TIPO_DOC_PER_DESCRIPCION}'