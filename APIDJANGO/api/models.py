from django.db import models

# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.EmailField()
    
class Encuesta(models.Model):
    Name = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)
    pregunta1 = models.CharField(max_length=100)
    Pregunta2 = models.CharField(max_length=100)
    Pregunta3 = models.CharField(max_length=100)
    Pregunta4 = models.CharField(max_length=100)
    Pregunta5 = models.CharField(max_length=100)
    Pregunta6 = models.CharField(max_length=100)
    Pregunta7 = models.CharField(max_length=100)
    Pregunta8 = models.CharField(max_length=100)
    Pregunta9 = models.CharField(max_length=100)
    Pregunta10 = models.CharField(max_length=100)
    Pregunta11 = models.CharField(max_length=100)
    
class Datos(models.Model):
    Fecha = models.CharField(max_length=100)
    Nombre = models.CharField(max_length=100)
    pregunta1 = models.CharField(max_length=100)
    Pregunta2 = models.CharField(max_length=100)
    Pregunta3 = models.CharField(max_length=100)
    Pregunta4 = models.CharField(max_length=100)
    Pregunta5 = models.CharField(max_length=100)
    Pregunta6 = models.CharField(max_length=100)
    Pregunta7 = models.CharField(max_length=100)
    Pregunta8 = models.CharField(max_length=100)
    Pregunta9 = models.CharField(max_length=100)
    Pregunta10 = models.CharField(max_length=100)
    
class Datoscsv(models.Model):
    Fecha = models.CharField(max_length=100)
    Nombre = models.CharField(max_length=100)
    pregunta1 = models.CharField(max_length=100)
    Pregunta2 = models.CharField(max_length=100)
    Pregunta3 = models.CharField(max_length=100)
    Pregunta4 = models.CharField(max_length=100)
    Pregunta5 = models.CharField(max_length=100)
    Pregunta6 = models.CharField(max_length=100)
    Pregunta7 = models.CharField(max_length=100)
    Pregunta8 = models.CharField(max_length=100)
    Pregunta9 = models.CharField(max_length=100)
    Pregunta10 = models.CharField(max_length=100)
    
  
    
    

    

    
    

    
 