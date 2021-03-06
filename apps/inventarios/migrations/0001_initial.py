# Generated by Django 4.0.2 on 2022-05-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('inv_id', models.AutoField(primary_key=True, serialize=False)),
                ('tienda', models.IntegerField(verbose_name='Tienda')),
                ('producto', models.IntegerField(verbose_name='Producto')),
                ('stock', models.IntegerField(verbose_name='Stock')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventario',
                'db_table': 'inventario',
            },
        ),
    ]
