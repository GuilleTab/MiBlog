from django.urls import path
from secciones.views import *

urlpatterns = [
    path("", index, name="inicio"),


]