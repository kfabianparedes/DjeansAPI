# Generated by Django 4.0.2 on 2022-07-06 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guias_de_remision', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guiaderemision',
            name='guia_flete',
        ),
    ]
