# Generated by Django 4.0.2 on 2022-04-17 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('mar_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('mar_descripcion', models.CharField(max_length=30)),
                ('mar_estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'db_table': 'marca',
            },
        ),
    ]