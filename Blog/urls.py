from django.contrib import admin
from django.urls import path

from .views import inicio, mi_template, listado_perros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name= "index"),
    path('listado-perros/', listado_perros, name="listado_perros"),
    path('mi-template/', mi_template),
    
    
    
]