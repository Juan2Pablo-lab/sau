from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
ciclos = [
   ('1', 'Primer Ciclo'), 
   ('2', 'Segundo Ciclo'), 
   ('3', 'Tercer Ciclo'), 
   ('4', 'Cuarto Ciclo'), 
   ('5', 'Quinto Ciclo'), 
   ('6', 'Sexto Ciclo'), 
   ('7', 'Septimo Ciclo'), 
   ('8', 'Octavo Ciclo'), 
   ('9', 'Noveno Ciclo'), 
   ('10', 'Decimo Ciclo'), 
]

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    duracion_ciclos = models.IntegerField()
    def __str__(self):
        return f'{self.nombre}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)
    correo = models.EmailField(max_length=50)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
3
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    horas = models.IntegerField()
    ciclo = models.IntegerField(null=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True) 
    def __str__(self):
        return f'{self.nombre}'

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)
    correo = models.EmailField(max_length=50)
    ciclo_culmidado = models.CharField(choices=ciclos, max_length=5, null=True, blank=True)
    ciclo = models.CharField(choices=ciclos, max_length=5, null=True, default='1')
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
