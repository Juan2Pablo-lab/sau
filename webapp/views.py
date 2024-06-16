from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError

# Create your views here.

def bienvenido(request):
    return render(request, 'bienvenido.html')

def registro(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"],email=request.POST["email"],password=request.POST["password1"])
                user.save()
                login(request,user)
                return redirect('carreras')
            except IntegrityError:
                return render(request, 'registro.html', {'formUsuario':UserCreationForm, 'error':'Error el usuario ya existe.'})
        return render(request, 'registro.html', {'formUsuario': UserCreationForm, 'error': 'Error, las contraseñas no coinciden'})
    return render(request, 'registro.html', {'formUsuario': UserCreationForm})

def iniciarSesion(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, 'iniciar.html', {'formUsuario': AuthenticationForm, 'error':'Error, el usuario o la contraseña no son validos.'})
        else:
            login(request, user)
            return redirect('carreras')
    return render(request, 'iniciar.html', {'formUsuario': AuthenticationForm})

def cerrarSesion(request):
    logout(request)
    return redirect('carreras')
