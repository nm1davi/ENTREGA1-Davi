
from re import template
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from datetime import datetime
from Blog.forms import FormPerro
from Blog.models import Perro
def inicio(request):
    return render(request, "index.html")


def listado_perros(request):
    lista_perros= Perro.objects.all()
    return render(request, "listado_perros.html", {"lista_perros": lista_perros})


def crear_perro(request):
    if request.method == 'POST':
        form = FormPerro(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            perro = Perro(
                nombre=data.get('nombre'),
                edad=data.get('edad'),
                fecha_creacion=data.get('fecha_creacion') if data.get('fecha_creacion') else datetime.now()
            )
            perro.save()
            return redirect('listado_perros')
        
        else:
            return render(request, 'crear_perro.html', {'form': form})
            
    
    form_perro = FormPerro()
    
    return render(request, "crear_perro.html", {'form': form_perro})