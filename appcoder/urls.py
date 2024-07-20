from django.urls import path

from appcoder.views import *

urlpatterns = [path("vista_inicio/", inicio),
    path("vista_estudiantes/", estudiantes),
    path("vista_profesores/", profesores),
    path("vista_entregables/", entregables),
    
]



