from pickle import TRUE
from django.db import models
from django.utils import timezone


class Mi_blog(models.Model):

    detalles = models.CharField(max_length=6000)
    logo = models.FileField()
    fecha_creacion = models.DateTimeField(auto_now_add=TRUE)
    fecha_actualizacion = models.DateTimeField(auto_now_add=TRUE)
