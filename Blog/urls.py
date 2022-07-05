
from django.urls import path
from .views import una_vista, crear_perro, listado_perros, mostrar_perro
urlpatterns = [
    path('', una_vista, name='index'),
    path('perros/', listado_perros, name='listado_perros'),
    path('crear-perro/', crear_perro, name='crear_perro'),
     path('mostrar-perro/<int:id>/', mostrar_perro, name='mostrar_perro')

]