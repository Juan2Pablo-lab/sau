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
from uni.views import verCarrera, inscribir, verAlumnos, matricula

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", bienvenido, name='index'),
    path("carreras/", verCarrera, name='carreras'),
    path("carreras/inscribir/<int:id>", inscribir, name='inscribir'),
    path("alumnos/", verAlumnos, name='alumnos'),
    path("alumnos/<int:id>", matricula, name='matricular'),
    path("iniciar_sesion/", iniciarSesion, name='registrar'),
    path("registrar/", registro, name='registrar'),
    path("cerrar_sesion/", cerrarSesion, name='cerrar_sesion'),
]
