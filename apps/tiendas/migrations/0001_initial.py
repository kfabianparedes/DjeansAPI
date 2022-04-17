# Generated by Django 4.0.2 on 2022-04-17 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('tie_id', models.AutoField(primary_key=True, serialize=False)),
                ('tie_nombre', models.CharField(max_length=50)),
                ('tie_estado', models.BooleanField(default=True)),
                ('sucursal', models.IntegerField(verbose_name='Sucursal')),
            ],
            options={
                'verbose_name': 'Tienda',
                'verbose_name_plural': 'Tiendas',
                'db_table': 'tienda',
            },
        ),
    ]
