# Generated by Django 4.1.7 on 2023-03-03 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProfile', '0003_editarusuario_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editarusuario',
            old_name='info_personal',
            new_name='descripcion',
        ),
    ]