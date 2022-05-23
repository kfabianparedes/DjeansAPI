# Generated by Django 4.0.2 on 2022-05-23 04:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo_comprobante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('comp_id', models.AutoField(primary_key=True, serialize=False)),
                ('comp_importe_total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Monto total')),
                ('comp_fecha_emision', models.DateField(verbose_name='Fecha emisión')),
                ('comp_fecha_registro', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha registro')),
                ('comp_serie', models.CharField(max_length=8, verbose_name='Nro. Serie')),
                ('comp_numero', models.CharField(max_length=8, verbose_name='Nro. comprobante')),
                ('comp_ingresada', models.BooleanField(default=False, verbose_name='Ingresada a tienda')),
                ('usuario', models.IntegerField(verbose_name='Usuario')),
                ('proveedor', models.IntegerField(verbose_name='Proveedor')),
                ('tipo_comprobante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tipo_comprobante', to='tipo_comprobante.tipocomprobante')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'db_table': 'compra',
            },
        ),
    ]
