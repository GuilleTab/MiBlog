from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout



def login_view(request):

    if request.method == "GET":
        formulario = AuthenticationForm()
        return render (request, "authentication/login.html", {"form": formulario})

    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return HttpResponse("Ud ha iniciado sesion correctamente")
        formulario = AuthenticationForm()
        return render (request, "authentication/login.html", {"form": formulario, "errores": ["Usuario incorrecto"]})


def register_view(request):
    if request.method == "GET":
        formulario = UserCreationForm()
        return render(request, "authentication/register.html", {"form": formulario})
    else:
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponse("Usuario creado correctamente")


def logout_view(request):
    logout(request)
    return HttpResponse("Cerraste sesion")
