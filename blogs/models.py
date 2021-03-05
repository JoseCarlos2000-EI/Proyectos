from django.db import models

# Create your models here.
class persona(models.Model):
    nombre=models.CharField(max_length=60)
    resumen=models.TextField()
    img=models.ImageField()
    correo=models.CharField(max_length=60)
    telefono=models.CharField(max_length=9)
    asuntoC=models.TextField()
    asuntoW=models.TextField()

    def __str__(self):
        return self.nombre

class Conocimiento(models.Model):
    nombrec=models.CharField(max_length=60)
    nivel=models.CharField(max_length=20)
    def __str__(self):
        return self.nombrec

class Proyecto(models.Model):
    nombrep=models.CharField(max_length=60)
    descrip=models.TextField()
    url=models.CharField(max_length=200)
    def __str__(self):
        return self.nombrep