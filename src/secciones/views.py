from django.views.generic import ListView, DetailView
from django.shortcuts import render
from secciones.models import Secciones


class Listado_secciones(ListView):
    model = Secciones