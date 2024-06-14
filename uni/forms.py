from django.forms import EmailInput, ModelForm, TextInput

from uni.models import Alumno


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