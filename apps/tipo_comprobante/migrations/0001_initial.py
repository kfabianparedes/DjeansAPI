# Generated by Django 4.0.2 on 2022-05-23 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoComprobante',
            fields=[
                ('tipo_comprobante_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_comprobante_descripcion', models.CharField(max_length=30, verbose_name='Tipo de comprobante')),
            ],
            options={
                'verbose_name': 'Tipo de comprobante',
                'verbose_name_plural': 'Tipo de comprobante',
                'db_table': 'tipo_comprobante',
            },
        ),
    ]
