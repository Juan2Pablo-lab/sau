"""
URL configuration for saa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import bienvenido, cerrarSesion, registro, iniciarSesion
from uni.views import verCarrera, inscribir, verAlumnos, matricula, nuevaCarrera, retirarAlumno, detalleCursos, buscarAlumno, nuevoCurso, verProfesores, nuevoProfesor

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", bienvenido, name='index'),
    path("profesores/", verProfesores, name='profesores'),
    path("nuevo_profesor/", nuevoProfesor, name='nuevo_profesor'),
    path("carreras/", verCarrera, name='carreras'),
    path("carreras/<int:id>", detalleCursos, name='detalle_cursos'),
    path("carreras/<int:id>/nuevo_curso", nuevoCurso, name='nuevo_curso'),
    path("nueva_carrera/", nuevaCarrera, name='nueva_carrera'),
    path("inscribir/<int:id>", inscribir, name='inscribir'),
    path("alumnos/", buscarAlumno, name='alumnos'),
    path("alumnos/<int:id>", matricula, name='matricular'),
    path("alumnos/<int:id>/retirar", retirarAlumno, name='retirar'),
    path("iniciar_sesion/", iniciarSesion, name='registrar'),
    path("registrar/", registro, name='registrar'),
    path("cerrar_sesion/", cerrarSesion, name='cerrar_sesion'),
]
