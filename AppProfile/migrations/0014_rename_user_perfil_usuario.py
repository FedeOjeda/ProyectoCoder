# Generated by Django 4.1.7 on 2023-03-05 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProfile', '0013_alter_perfil_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='user',
            new_name='usuario',
        ),
    ]