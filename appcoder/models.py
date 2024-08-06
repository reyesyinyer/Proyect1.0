from django.db import models



class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    
    def __str__(self):
        return f"Nombre del Curso: {self.nombre} -Numero de Comision: {self.comision} "

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre del Alumno: {self.nombre} -Apellido del Alumno: {self.apellido} - Email del Alumno: {self.email} "


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre del Profesor: {self.nombre} -Apellido del Profesor: {self.apellido} - Email del Profesor: {self.email} - Profesion del Profesor: {self.profesion} "


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    
    def __str__(self):
        return f"Nombre del Entregable: {self.nombre} -Fecha del entregable: {self.fecha_de_entrega} - Entregado: {self.entregado} "