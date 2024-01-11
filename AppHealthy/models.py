from django.db import models

# Create your models here.

class Frutosecos(models.Model):
    nombre = models.CharField(max_length=40)
    presentacion = models.CharField(max_length=40)
    precio = models.FloatField()

class Semillas(models.Model):
    nombre = models.CharField(max_length=40)
    presentacion = models.CharField(max_length=40)
    precio = models.FloatField()

class Especias(models.Model):
    nombre = models.CharField(max_length=40)
    presentacion = models.CharField(max_length=40)
    precio = models.FloatField()

