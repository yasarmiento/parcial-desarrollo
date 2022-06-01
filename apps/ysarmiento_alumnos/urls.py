from django.urls import path
from apps.ysarmiento_alumnos import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('create/', views.create, name = 'create'),
]   