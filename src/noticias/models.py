from pickle import TRUE
from django.db import models
from django.utils import timezone


class Entradas(models.Model):

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.FileField()
    fecha_creacion = models.DateTimeField(auto_now_add=TRUE)
    fecha_actualizacion = models.DateTimeField(auto_now_add=TRUE)
