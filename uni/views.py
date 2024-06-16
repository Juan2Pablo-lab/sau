from django.shortcuts import get_object_or_404, render, redirect
from uni.forms import AlumnoForm, MatriculaForm, CarreraForm, CursoForm, ProfesorForm
from uni.models import Carrera, Curso, Alumno, Profesor
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def verCarrera(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras/ver.html', {'carreras': carreras})

def nuevaCarrera(request):
    if request.method == 'POST':
        formCarrera = CarreraForm(request.POST)
        if formCarrera.is_valid():
            formCarrera.save()
            return redirect('carreras')
    else:
        formCarrera = CarreraForm()
    return render(request, 'carreras/nuevo.html', {'formCarrera': formCarrera})

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

def buscarAlumno(request):
    buscar = request.GET.get('buscar')
    alumnos = Alumno.objects.all()
    if buscar:
        alumnos = Alumno.objects.filter(id=buscar)
        return render(request, 'alumnos/buscar.html', {'alumnos':alumnos})
    else:
        return render(request, 'alumnos/buscar.html', {'alumnos':alumnos})

def matricula(request, id):
    alumno = get_object_or_404(Alumno, pk=id)
    if request.method == 'POST':
        formMatricula = MatriculaForm(request.POST, instance=alumno)
        if formMatricula.is_valid():
            formMatricula.save()
            return redirect('alumnos')
    else:
        formMatricula = MatriculaForm(instance=alumno)
    return render(request, 'alumnos/matricular.html', {'formMatricula': formMatricula, 'alumno':alumno})

def retirarAlumno(request, id):
    alumno = get_object_or_404(Alumno, pk=id)
    if request.method == 'POST':
        if alumno:
            alumno.delete()
            return redirect('alumnos')
    else:
        return render(request, 'alumnos/retirar.html', {'alumno': alumno})

def detalleCursos(request, id):
    carrera = get_object_or_404(Carrera, pk=id)
    buscar = request.GET.get('buscar')
    cursos = Curso.objects.filter(carrera_id=id)
    if buscar:
        cursos = Curso.objects.filter(ciclo=buscar)
        return render(request, 'cursos/detalle.html', {'cursos': cursos, 'carrera': carrera})
    else: 
        return render(request, 'cursos/detalle.html', {'cursos': cursos, 'carrera': carrera})

def nuevoCurso(request, id):
    carrera = get_object_or_404(Carrera, pk=id)
    if request.method == 'POST':
        formCurso = CursoForm(request.POST)
        if formCurso:
            nuevo = formCurso.save(commit=False)
            nuevo.carrera = carrera
            nuevo.save()
            return redirect('carreras')
    else:
        formCurso = CursoForm()
    return render(request, 'cursos/nuevo.html', {'formCurso': formCurso})

def verProfesores(request):
    buscar = request.GET.get('buscar')
    profesores = Profesor.objects.all()
    if buscar:
        profesores = Profesor.objects.filter(id=buscar)
        return render(request, 'profesores/ver.html', {'profesores': profesores})
    return render(request, 'profesores/ver.html', {'profesores': profesores})

def nuevoProfesor(request):
    if request.method == 'POST':
        formProfesor = ProfesorForm(request.POST)
        if formProfesor:
            formProfesor.save()
            return redirect('profesores')
    else:
        formProfesor = ProfesorForm()
    return render(request, 'profesores/nuevo.html', {'formProfesor': formProfesor})
