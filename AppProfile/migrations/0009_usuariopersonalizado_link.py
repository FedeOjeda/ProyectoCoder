# Generated by Django 4.1.7 on 2023-03-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProfile', '0008_alter_usuariopersonalizado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariopersonalizado',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]