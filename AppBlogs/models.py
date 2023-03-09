from django.db import models
from django.contrib.auth.models import User

# Modelo del Blog.
class Blogs(models.Model):
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='imagen-blog', null=True, blank=True)
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Blogs'
