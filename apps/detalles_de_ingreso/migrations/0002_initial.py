# Generated by Django 4.0.2 on 2022-07-06 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        ('detalles_de_ingreso', '0001_initial'),
        ('nota_de_ingreso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalledeingreso',
            name='nota_de_ingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nota_de_ingreso', to='nota_de_ingreso.notadeingreso'),
        ),
        migrations.AddField(
            model_name='detalledeingreso',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='productos.producto'),
        ),
    ]
