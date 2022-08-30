from django.shortcuts import render
from noticias.models import Entradas

def index(request):
    return render(request, "noticias/base.html")