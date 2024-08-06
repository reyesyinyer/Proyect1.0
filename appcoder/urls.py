from django.urls import path

from appcoder.views import *

from appcoder import views

urlpatterns = [path("", views.inicio, name="inicio"),
    path("vista_cursos/", views.cursos, name="cursos"),
    path("vista_estudiantes/", views.estudiantes, name="estudiantes"),
    path("vista_profesores/", views.profesores, name="profesores"),
    path("vista_entregables/", views.entregables, name="entregables"),
    path("vista_formularios", views.formulariocurso, name="formulariocurso"),
    path("formularios_estudiantes", views.formularioestudiantes, name="formularioestudiantes"),
    path("formularios_profesores", views.formularioprofesores, name="formularioprofesores"),
    path("formularios_entregables", views.formularioentregables, name="formularioentregables"),
    path("buscarcomision/", views.buscarcomision, name="Buscarcomision"),
    path("buscar/", views.buscar),
    
    
]




