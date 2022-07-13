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
            return render(request, 'auto/crear_auto.html', {'form': form})
            
    
    form_Auto = FormAuto()
    
    return render(request, 'auto/crear_auto.html', {'form': form_Auto})

def listado_Autos(request):
    
    marca_de_busqueda = request.GET.get('marca')
    
    if marca_de_busqueda:
        listado_Autos = Auto.objects.filter(marca__icontains=marca_de_busqueda) 
    else:
        listado_Autos = Auto.objects.all()
    
    form = BusquedaAuto()
    return render(request, 'auto/listado_autos.html', {'listado_Autos': listado_Autos, 'form': form})

def editar_Auto(request, id):
    auto = Auto.objects.get(id=id)
    if request.method == 'POST':
        form = FormAuto(request.POST)
        if form.is_valid():
            auto.marca = form.cleaned_data.get("marca")
            auto.modelo = form.cleaned_data.get("modelo")
            auto.fecha_creacion = form.cleaned_data.get("fecha_creacion")
            auto.save()
            return redirect('listado_Autos')
        else:
            return render(request, 'auto/editar_auto.html', {'form': form, "auto": auto} )

 
    form_Auto = FormAuto(initial={"marca": auto.marca , "modelo": auto.modelo , "fecha_creacion": auto.fecha_creacion})
    
    return render(request, 'auto/editar_auto.html', {'form': form_Auto, "auto": auto})
    
    
def eliminar_Auto(request, id):
    auto = Auto.objects.get(id=id)
    auto.delete()
    return redirect('listado_Autos')

def mostrar_Auto(request, id):
    auto = Auto.objects.get(id=id)
    return render(request, "auto/mostrar_auto.html", {"auto": auto})