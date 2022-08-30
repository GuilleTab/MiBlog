from django.urls import path
from noticias.views import *

urlpatterns = [
    path("", index, name="inicio"),


]