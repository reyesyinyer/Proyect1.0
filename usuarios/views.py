from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import	*

import requests

def login_request(request):
    msg_login = ""

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                print(f"\n INICIO DE SESION EXITOSO \n")
                return render(request, "appcoder/inicio.html")
                
            
        msg_login = "Datos incorrectos de inicio sesion"

    form = AuthenticationForm()

    return render(request, "usuarios/login.html", {"form": form, "msg_login":msg_login})

def register(request):
    
    msg_register = ""
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
        
            form.save()
            
            return render(request, "appcoder/inicio.html")
        
        msg_register = "Error en los datos ingresados"
        
    form = UserRegisterForm()
    
    return render(request, "usuarios/register.html", {"form":form, "msg_register":msg_register})
