from django.shortcuts import render, redirect
from apps.ysarmiento_alumnos.formalumnos import Alumnosform
from apps.ysarmiento_alumnos.models import Alumnos

# Create your views here.

def inicio(request):    
    alumnos = Alumnos.objects.all().order_by('id')
    return render(request,'paginas/alumnos.html', {'alumnos': alumnos})

def create(request):
    if request.method == 'POST':
        form = Alumnosform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = Alumnosform()
        return render(request,'paginas/alumnosform.html', {'form': form})