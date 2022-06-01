from django.db import models

# Create your models here.

class Grupos (models.Model):
    nombre = models.CharField(max_length=30)
    salon = models.CharField(max_length=30)
    
    def __str__(self):
        return self.salon