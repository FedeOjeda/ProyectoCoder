# Generated by Django 4.1.7 on 2023-03-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProfile', '0027_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfiles',
            name='imagen',
            field=models.ImageField(blank=True, default='blank.png', null=True, upload_to='avatares'),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
