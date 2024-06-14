from django.contrib import admin
from uni.models import Carrera, Profesor, Curso, Alumno

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Alumno)