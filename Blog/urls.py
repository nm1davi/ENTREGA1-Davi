
from django.urls import path
from .views import una_vista, crear_Auto, listado_Autos, acerca_de_nosotros
urlpatterns = [
    path('', una_vista, name='index'),
    path('about/', acerca_de_nosotros, name='acerca_de_nosotros'),
    path('Autos/', listado_Autos, name='listado_Autos'),
    path('crear-Auto/', crear_Auto, name='crear_Auto'),

]