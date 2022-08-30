from pickle import TRUE
from django.db import models
from django.utils import timezone


class Secciones(models.Model):

    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=TRUE)
    fecha_actualizacion = models.DateTimeField(auto_now_add=TRUE)