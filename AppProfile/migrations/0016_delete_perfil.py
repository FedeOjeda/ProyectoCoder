# Generated by Django 4.1.7 on 2023-03-05 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProfile', '0015_rename_usuario_perfil_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
