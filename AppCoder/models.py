from django.db import models

# Create your models here.
class Curso(models.Model):
    
    # CharField es para string(str)
    nombres = models.CharField(max_length=40)
    
    # CharField es para números enteros(int)
    camada = models.IntegerField()
    
class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    
    # emailField es para datos tipo email
    email = models.EmailField()

class Profesor(models.Model):
    
   nombre = models.CharField(max_length=30)
   apellido = models.CharField(max_length=30)
   email = models.EmailField()
   profesion = models.CharField(max_length=30)
    
class Entregable(models.Model):
    
    nombre = models.CharField(max_length=40)
    
    # DateField es para datos tipo fecha
    fecha_de_entrega = models.DateField()
   
   # BooleanField es para booleanos(bool)
    entregado = models.BooleanField()
    
    