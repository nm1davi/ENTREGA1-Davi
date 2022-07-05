from django.contrib import admin
from django.urls import path

from .views import inicio, listado_perros, crear_perro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name= "index"),
    path('listado-perros/', listado_perros, name="listado_perros"),
    path('crear-perros/', crear_perro, name="crear_perro"),
    
    
    
    
]