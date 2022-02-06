# Generated by Django 4.0 on 2022-02-06 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SUCURSALES',
            fields=[
                ('SUC_ID', models.AutoField(primary_key=True, serialize=False, verbose_name='SUC_ID')),
                ('SUC_NOMBRE', models.CharField(max_length=50)),
                ('SUC_DIRECCION', models.CharField(max_length=50)),
                ('SUC_ESTADO', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'sucursal',
                'ordering': ['SUC_ID'],
            },
        ),
    ]