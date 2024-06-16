from django.forms import EmailInput, ModelForm, TextInput

from uni.models import Alumno, Carrera, Curso, Profesor


class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni', 'correo']
        widgets = {
            'correo': EmailInput(attrs={'type':'email'}),
            'dni': TextInput(attrs={'type':'number'})
        }

class MatriculaForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni', 'correo', 'ciclo_culmidado', 'ciclo']
        widgets = {
            'correo': EmailInput(attrs={'type':'email'}),
            'dni': TextInput(attrs={'type':'number'})
        }

class CarreraForm(ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'creditos', 'horas', 'ciclo', 'profesor']
        widgets = {
            'creditos': TextInput(attrs={'type':'number'}),
            'horas': TextInput(attrs={'type':'number'}),
            'ciclo': TextInput(attrs={'type':'number'})
        }

class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
        widgets = {
            'correo' : EmailInput(attrs={'type': 'email'})
        }