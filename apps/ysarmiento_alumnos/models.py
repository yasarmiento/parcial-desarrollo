from django.db import models
from apps.ysarmiento_grupos.models import Grupos

# Create your models here.

class Alumnos (models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    idgrupos = models.ForeignKey(Grupos, on_delete=models.CASCADE)