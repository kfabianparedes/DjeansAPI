# Generated by Django 4.0.2 on 2022-04-04 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marcas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marca',
            old_name='mar_descripcion',
            new_name='mar_descripcione',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='mar_estado',
            new_name='mar_estadoe',
        ),
        migrations.AlterModelTable(
            name='marca',
            table='marcaquita',
        ),
    ]