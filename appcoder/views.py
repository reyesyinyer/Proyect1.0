from django.shortcuts import render
from django.http import HttpResponse
from .models import	*
from appcoder.forms import MiFormulario
from appcoder.forms import MiFormularioEstudiantes
from appcoder.forms import MiFormularioProfesores
from appcoder.forms import MiFormularioEntregables
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 

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
    if request.method == 'POST':
        formulario = MiFormularioProfesores(request.POST)
        
        
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            profesores = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
            profesores.save()
            return render(request, "appcoder/profesores.html")
    else:
        formulario = MiFormularioProfesores()
        
    return render(request, "appcoder/formularioprofesores.html", {"formulario": formulario})

def leerProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {"profesores":profesores}
    
    return render(request, "appcoder/leerprofesores.html", contexto)

def editarProfesor(request, profesor_id):
    
    profesor = Profesor.objects.get(id =profesor_id)
    
    if request.method == 'POST':
        
        miFormulario = MiFormularioProfesores(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            
            profesor.save()
            
            return render(request, "appcoder/inicio.html")
    else:
        miFormulario = MiFormularioProfesores(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
        
    return render(request, "appcoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_id":profesor_id})

def eliminarProfesor(request, profesor_nombre):
    
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    
    profesor.delete() ##esto sirve para borrar
    
    profesores = Profesor.objects.all()
    
    contexto = {"profesores":profesores}
    
    return render(request, "appcoder/leerprofesores.html", contexto)

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

class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "appcoder/listar.html"
    
class CursoCreateView(CreateView):
    model = Curso
    template_name = "appcoder/crear.html"
    success_url = reverse_lazy('ListarCursos')
    fields = ['nombre','comision']
    
class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "appcoder/actualizar.html"
    success_url = reverse_lazy('ListarCursos')
    fields = ['nombre','comision']
    
class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "appcoder/borrar.html"
    success_url = reverse_lazy('ListarCursos')
    fields = ['nombre','comision']
    
class CursoDetailView(DetailView):
    model = Curso
    template_name = "appcoder/ver.html"
    





