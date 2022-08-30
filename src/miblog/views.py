from django.shortcuts import render
from miblog.models import Mi_blog

def index(request):
    return render(request, "noticias/base.html")