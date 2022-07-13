from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from mascota.models import Gato
from django.views.generic import DetailView


class ListadoGatos(ListView):
    model=Gato
    template_name = "gato/listado_gatos.html"
   
    
class CrearGato(CreateView):
    model=Gato
    template_name = "gato/crear_gato.html"
    success_url = "/mascota/gatos"
    fields = ["apodo", "edad", "fecha_creacion"]
    
class EditarGato(UpdateView):
    model=Gato
    template_name = "gato\editar_gato.html"
    success_url = "/mascota/gatos"
    fields = ["apodo", "edad", "fecha_creacion"]
    
class EliminarGato(DeleteView):
    model=Gato
    template_name = "gato/eliminar_gato.html"
    success_url = "/mascota/gatos"
class MostrarGato (DetailView):
    model = Gato
    template_name = "gato/mostrar_gato.html"