from django.urls import path
from miblog.views import *

urlpatterns = [
    path("", index, name="inicio"),


]
