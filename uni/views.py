from django.shortcuts import get_object_or_404, render, redirect
from uni.forms import AlumnoForm, MatriculaForm
from uni.models import Carrera, Curso, Alumno

# Create your views here.

def verCarrera(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras/ver.html', {'carreras': carreras})

def detalleCurso(request, id):
    carrera = get_object_or_404(Carrera, pk=id)
    cursos = Curso.objects.filter(carrera_id=id)
    return render(request, 'cursos/detalle.html', {'carrera':carrera, 'cursos': cursos})

def inscribir(request, id):
    carrera = get_object_or_404(Carrera, pk=id)
    if request.method == 'POST':
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            inscripcion = formAlumno.save(commit=False)
            inscripcion.carrera = carrera
            inscripcion.save()
            return redirect('carreras')
    else:
        formAlumno = AlumnoForm()
    return render(request, 'alumnos/inscribir.html', {'formAlumno': formAlumno, 'carrera':carrera})

def verAlumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/ver.html', {'alumnos': alumnos})

def matricula(request, id):
    alumno = get_object_or_404(Alumno, pk=id)
    if request.method == 'POST':
        formMatricula = MatriculaForm(request.POST, instance=alumno)
        if formMatricula.is_valid():
            formMatricula.save()
            return redirect('carreras')
    else:
        formMatricula = MatriculaForm(instance=alumno)
    return render(request, 'alumnos/matricular.html', {'formMatricula': formMatricula, 'alumno':alumno})