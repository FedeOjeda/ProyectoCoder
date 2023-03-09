from django.contrib.auth.models import User
from django.db import models

# Modelo del perfil.
class Perfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    link = models.URLField(blank=True)
    imagen = models.ImageField(upload_to='imagen-perfil', null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name_plural = 'Perfiles'

# Modelo del avatar.   
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='imagen-avatar', null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name_plural = 'Avatares'
    