# Generated by Django 4.1.7 on 2023-03-04 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppProfile', '0007_alter_usuariopersonalizado_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuariopersonalizado',
            options={},
        ),
        migrations.AlterModelManagers(
            name='usuariopersonalizado',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='usuariopersonalizado',
            old_name='descripcion',
            new_name='bio',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='link',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='usern',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='username',
        ),
        migrations.AddField(
            model_name='usuariopersonalizado',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
        migrations.AddField(
            model_name='usuariopersonalizado',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ContraseñaPersonalizada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contraseña1', models.CharField(max_length=40)),
                ('contraseña2', models.CharField(max_length=40)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
