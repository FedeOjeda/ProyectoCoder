# Generated by Django 4.1.7 on 2023-03-05 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProfile', '0011_rename_usuariopersonalizado_perfil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='imagen',
            new_name='avatar',
        ),
    ]
