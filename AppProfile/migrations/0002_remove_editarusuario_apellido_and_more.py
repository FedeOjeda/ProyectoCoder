# Generated by Django 4.1.7 on 2023-03-03 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProfile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editarusuario',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='editarusuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='editarusuario',
            name='nombre',
        ),
    ]
