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
    path("leerprofesores/", views.leerProfesores, name="LeerProfesores"),
    path("eliminarProfesor/<profesor_nombre>", views.eliminarProfesor, name="EliminarProfesores"),
    path("editarProfesor/<profesor_id>/", views.editarProfesor, name="EditarProfesores"),
    path("listar/", views.CursoListView.as_view(), name="ListarCursos"),
    path("crear/", views.CursoCreateView.as_view(), name="CrearCursos"),
    path("actualizar/<pk>", views.CursoUpdateView.as_view(), name="ActualizarCursos"),
    path("borrar/<pk>", views.CursoDeleteView.as_view(), name="BorrarCursos"),
    path("ver/<pk>", views.CursoDetailView.as_view(), name="VerCursos"),
    
    
]




