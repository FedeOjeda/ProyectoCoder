# Generated by Django 4.1.7 on 2023-03-08 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogs', '0009_remove_mensajes_nombre_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='AppBlogs.blogs'),
        ),
    ]
