from django import forms
from apps.ysarmiento_alumnos.models import Alumnos

class Alumnosform(forms.ModelForm):
    class Meta:
        model= Alumnos
        
        fields = {
            'nombre',
            'direccion',
            'telefono',
            'correo',
            'idgrupos',
        }
        
        labels = {
            'nombre': 'ingrese el nombre del alumno',
            'direccion': 'ingrese la direccion del alumno',
            'telefono': 'ingrese el numero de telefono del alumno',
            'correo': 'ingrese el correo del alumno',
            'idgrupos': 'seleccione el grupo',
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs= {'class': 'form-control'}),
            'direccion': forms.TextInput(attrs= {'class': 'form-control'}),
            'telefono': forms.TextInput(attrs= {'class': 'form-control'}),
            'correo': forms.TextInput(attrs= {'class': 'form-control'}),
            'idgrupos': forms.Select(attrs= {'class': 'form-control'}),
        }