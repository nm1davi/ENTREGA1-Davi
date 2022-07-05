from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import BusquedaAuto, FormAuto
from .models import Auto
from datetime import datetime


def acerca_de_nosotros(request):
    return render(request, 'about.html')

def una_vista(request):
    return render(request, 'index.html')

def crear_Auto(request):
    if request.method == 'POST':
        form = FormAuto(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            auto = Auto(
                marca=data.get('marca'),
                modelo=data.get('modelo'),
                fecha_creacion=data.get('fecha_creacion') if data.get('fecha_creacion') else datetime.now()
            )
            auto.save()
            return redirect('listado_Autos')
        
        else:
            return render(request, 'crear_auto.html', {'form': form})
            
    
    form_Auto = FormAuto()
    
    return render(request, 'crear_auto.html', {'form': form_Auto})

def listado_Autos(request):
    
    marca_de_busqueda = request.GET.get('marca')
    
    if marca_de_busqueda:
        listado_Autos = Auto.objects.filter(marca__icontains=marca_de_busqueda) 
    else:
        listado_Autos = Auto.objects.all()
    
    form = BusquedaAuto()
    return render(request, 'listado_autos.html', {'listado_Autos': listado_Autos, 'form': form})

