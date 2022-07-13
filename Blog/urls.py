
from django.urls import path
from .views import una_vista, crear_Auto, listado_Autos, acerca_de_nosotros, editar_Auto, eliminar_Auto, mostrar_Auto
urlpatterns = [
    path('', una_vista, name='index'),
    path('about/', acerca_de_nosotros, name='acerca_de_nosotros'),
    path('Autos/', listado_Autos, name='listado_Autos'),
    path('crear-Auto/', crear_Auto, name='crear_Auto'),
    path('editar-Auto/<int:id>/', editar_Auto, name='editar_Auto'),
    path('eliminar-Auto/<int:id>/', eliminar_Auto, name='eliminar_Auto'),
    path('mostrar-Auto/<int:id>/', mostrar_Auto, name='mostrar_Auto'),
    

]