from django.forms import forms
from django import forms


class MiFormulario(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()
    
class MiFormularioEstudiantes(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
class MiFormularioProfesores(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    
class MiFormularioEntregables(forms.Form):
    nombre = forms.CharField()
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField()
    
