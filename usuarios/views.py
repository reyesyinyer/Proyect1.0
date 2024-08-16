from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from usuarios.forms import UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.urls import path
from .forms import	*

import requests
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    template_name = 'usuarios/logout.html'


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


@login_required
def editarperfil(request):
    usuario = request.user
    
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if mi_formulario.is_valid():
            
            if mi_formulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = mi_formulario.cleaned_data.get('imagen')
                usuario.avatar.save()
            
            mi_formulario.save()
            return render(request, "appcoder/inicio.html")
    else:
        mi_formulario = UserEditForm(instance=usuario)
        
        return render(request, "usuarios/editarperfil.html", {"form":mi_formulario})
    
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "usuarios/editarpassword.html"
    success_url = reverse_lazy("EditarPerfil")
