# Generated by Django 4.0.2 on 2022-02-06 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_usuario_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('ESTADO_CIVIL_ID', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Estado Civil ID')),
                ('ESTADO_CIVIL_DESCRIPCION', models.CharField(max_length=30, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Estado Civil',
                'verbose_name_plural': 'Estados Civiles',
                'db_table': 'estado_civil',
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('TIPO_DOC_PER_ID', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Tipo de documento - ID')),
                ('TIPO_DOC_PER_DESCRIPCION', models.CharField(max_length=30, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo documento personal',
                'verbose_name_plural': 'Tipos de documentos personales',
                'db_table': 'tipo_documento_personal',
            },
        ),
        migrations.CreateModel(
            name='InformacionPersonal',
            fields=[
                ('INFO_PER_ID', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Inf. Personal Nº')),
                ('INFO_PER_NOMBRES', models.CharField(blank=True, max_length=50, null=True)),
                ('INFO_PER_APELLIDOS', models.CharField(blank=True, max_length=50, null=True)),
                ('INFO_PER_EMAIL', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('INFO_PER_GENERO', models.CharField(default='F', max_length=1)),
                ('INFO_PER_FECHA_NACIMIENTO', models.DateField(blank=True, null=True)),
                ('INFO_PER_DIRECCION1', models.TextField(blank=True, max_length=100, null=True)),
                ('INFO_PER_DIRECCION2', models.TextField(blank=True, max_length=100, null=True)),
                ('INFO_PER_CELULAR1', models.CharField(blank=True, max_length=9, null=True)),
                ('INFO_PER_CELULAR2', models.CharField(blank=True, max_length=9, null=True)),
                ('INFO_PER_DOCUMENTO_IDENTIDAD', models.CharField(blank=True, max_length=11, null=True)),
                ('ESTADO_CIVIL_ID', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.estadocivil')),
                ('TIPO_DOC_PER_ID', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.tipodocumento')),
                ('USU_ID', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Información Personal',
                'verbose_name_plural': 'Informaciones personales',
                'db_table': 'informacion_personal',
            },
        ),
    ]
