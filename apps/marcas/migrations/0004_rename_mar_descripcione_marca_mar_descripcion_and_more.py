# Generated by Django 4.0.2 on 2022-04-04 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marcas', '0003_rename_mar_id_marca_mar_ide'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marca',
            old_name='mar_descripcione',
            new_name='mar_descripcion',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='mar_estadoe',
            new_name='mar_estado',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='mar_ide',
            new_name='mar_id',
        ),
        migrations.AlterModelTable(
            name='marca',
            table='marca',
        ),
    ]