from django.urls import path
from . import views

urlpatterns = [
    path('', views.laboratorio_mostrar, name='mostrar_laboratorios'),
    path('agregar/', views.laboratorio_insertar, name='insertar_laboratorio'),
    path('<int:pk>/editar/', views.laboratorio_editar, name='editar_laboratorio'),
    path('<int:pk>/eliminar/', views.laboratorio_eliminar, name='eliminar_laboratorio'),
]
