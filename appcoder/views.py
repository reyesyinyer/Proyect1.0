from django.shortcuts import render
from django.http import HttpResponse
from .models import	*
from appcoder.forms import MiFormulario
from appcoder.forms import MiFormularioEstudiantes
from appcoder.forms import MiFormularioProfesores
from appcoder.forms import MiFormularioEntregables
import requests

def inicio(request):
    return render(request, "appcoder/inicio.html")

def cursos(request):
    
    cursos = Curso.objects.all()
    
    return render(request, "appcoder/cursos.html", {"cursos":cursos})

def estudiantes(request):
    
    estudiantes = Estudiante.objects.all()
    
    return render(request, "appcoder/estudiantes.html", {"estudiantes":estudiantes})

def profesores(request):
    
    profesores = Profesor.objects.all()
    
    return render(request, "appcoder/profesores.html", {"profesores":profesores})


def entregables(request):
    
    entregables = Entregable.objects.all()
    
    return render(request, "appcoder/entregables.html", {"entregables":entregables})


def formularioestudiantes(request):
    if request.method == "POST":
        formulario = MiFormularioEstudiantes(request.POST)
        
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiantes = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiantes.save()
            return render(request, "appcoder/estudiantes.html")
    else:
        formulario = MiFormularioEstudiantes()
        
    return render(request, "appcoder/formularioestudiantes.html", {"formulario": formulario})

def formulariocurso(request):
    if request.method == "POST":
        formulario = MiFormulario(request.POST)
        
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            curso = Curso(nombre=informacion["nombre"], comision=informacion["comision"])
            curso.save()
            return render(request, "appcoder/cursos.html")
    else:
        formulario = MiFormulario()
        
    return render(request, "appcoder/formulariocurso.html", {"formulario": formulario})

def formularioprofesores(request):
    if request.method == "POST":
        formulario = MiFormularioProfesores(request.POST)
        
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            profesores = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
            profesores.save()
            return render(request, "appcoder/profesores.html")
    else:
        formulario = MiFormularioProfesores()
        
    return render(request, "appcoder/formularioprofesores.html", {"formulario": formulario})

def formularioentregables(request):
    if request.method == "POST":
        formulario = MiFormularioEntregables(request.POST)
        
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            entregables = Entregable(nombre=informacion["nombre"], fecha_de_entrega=informacion["fecha_de_entrega"], entregado=informacion["entregado"])
            entregables.save()
            return render(request, "appcoder/entregables.html")
    else:
        formulario = MiFormularioEntregables()
        
    return render(request, "appcoder/formularioentregables.html", {"formulario": formulario})



def buscarcomision(request):
    return render(request, "appcoder/buscarcomision.html")

def buscar(request):
    
    if request.GET["comision"]:
    
        ##respuesta = f"Estoy buscando la comision nro: {request.GET["comision"] }"
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, "appcoder/resultadosBusqueda.html", {"cursos":cursos, "comision":comision})

    else:
    
        respuesta= "No enviar datos"    
    
    
    return HttpResponse(respuesta)
    
    