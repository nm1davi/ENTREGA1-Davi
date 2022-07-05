
from re import template
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from Blog.models import Perro
def inicio(request):
    return render(request, "index.html")

def mi_template (request):
    
    template1= loader.get_template("prueba.html")
    
    perro= Perro(nombre= "Rocho", edad= 15)
    perro.save()
    render1= template1.render({"perro": perro})
    return HttpResponse(render1)

def listado_perros(request):
    lista_perros= Perro.objects.all()
    return render(request, "listado_perros.html", {"lista_perros": lista_perros})