from django.shortcuts import redirect, render

from .forms import BusquedaPerro, FormPerro
from .models import Perro
from datetime import datetime


def una_vista(request):
    return render(request, 'index.html')

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
    
    return render(request, 'crear_perro.html', {'form': form_perro})

def listado_perros(request):
    
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        listado_perros = Perro.objects.filter(nombre__icontains=nombre_de_busqueda) 
    else:
        listado_perros = Perro.objects.all()
    
    form = BusquedaPerro()
    return render(request, 'listado_perros.html', {'listado_perros': listado_perros, 'form': form})

def mostrar_perro(request, id):
    perro = Perro.objects.get(id=id)
    return render(request, 'perro/mostrar_perro.html', {'perro': perro})