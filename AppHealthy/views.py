from django.shortcuts import render
from AppHealthy.models import Frutosecos, Semillas, Especias
from AppHealthy.forms import FrutosecoFormulario, SemillaFormulario, EspeciaFormulario
from AppHealthy.views import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    
    return render(request, "AppHealthy/inicio.html")

def ver_frutos(request):
     
    if request.method == "GET":
        
        ver_frutoseco = Frutosecos.objects.all()
    
        return render(request, "AppHealthy/frutos.html", {"frutos": ver_frutoseco})

    else:
        return render(request, "AppHealthy/frutos.html")
    
def ver_semillas(request):

    if request.method == "GET":
        
        ver_semillas = Semillas.objects.all()
    
        return render(request, "AppHealthy/semillas.html", {"semillas": ver_semillas})

    else:
        return render(request, "AppHealthy/semillas.html")

def ver_especias(request):

    if request.method == "GET":
        
        ver_especias = Especias.objects.all()
    
        return render(request, "AppHealthy/especias.html", {"especia": ver_especias})

    else:
        return render(request, "AppHealthy/especias.html")
    
def agregar_frutos(request):

    if request.method == "POST":

        nuevo_formulario = FrutosecoFormulario(request.POST)
    
        if nuevo_formulario.is_valid():
            
            info = nuevo_formulario.cleaned_data
            
            fruto_nuevo = Frutosecos(nombre=info["nombre"], presentacion=info["presentacion"], precio=info["precio"])

            fruto_nuevo.save()

            return render(request, "AppHealthy/inicio.html")
        
    else:
        nuevo_formulario = FrutosecoFormulario
        
    return render(request, "AppHealthy/nuevo_fruto.html", {"mi_formu": nuevo_formulario})

def busqueda_frutoseco(request):

    return render(request, "AppHealthy/busqueda_frutoseco.html")

def resultado_buscarfrutoseco(request):

    if request.method == "GET":

        nombre_buscado = request.GET["buscafruto"]
        
        resultados_frutoseco = Frutosecos.objects.filter(nombre__icontains=nombre_buscado)
    
        return render(request, "AppHealthy/busqueda_frutoseco.html", {"frutos":resultados_frutoseco})

    else:
        return render(request, "AppHealthy/busqueda_frutoseco.html")
    
def agregar_semilla(request):

    if request.method == "POST":

        nuevo_formulario1 = SemillaFormulario(request.POST)
    
        if nuevo_formulario1.is_valid():
            
            info1 = nuevo_formulario1.cleaned_data
            
            semilla_nuevo = Semillas(nombre=info1["nombre"], presentacion=info1["presentacion"], precio=info1["precio"])

            semilla_nuevo.save()

            return render(request, "AppHealthy/inicio.html")
        
    else:
        nuevo_formulario1 = SemillaFormulario
        
    return render(request, "AppHealthy/nueva_semilla.html", {"mi_formu1": nuevo_formulario1})

def busqueda_semilla(request):

    return render(request, "AppHealthy/busqueda_semilla.html")

def resultado_buscarsemilla(request):

    if request.method == "GET":

        nombre_buscado = request.GET["buscasemilla"]
        
        resultados_semillas = Semillas.objects.filter(nombre__icontains=nombre_buscado)
    
        return render(request, "AppHealthy/busqueda_semilla.html", {"semilla": resultados_semillas})

    else:
        return render(request, "AppHealthy/busqueda_semilla.html")

def agregar_especias(request):

    if request.method == "POST":

        nuevo_formulario2 = EspeciaFormulario(request.POST)
    
        if nuevo_formulario2.is_valid():
            
            info2 = nuevo_formulario2.cleaned_data
            
            especia_nuevo = Especias(nombre=info2["nombre"], presentacion=info2["presentacion"], precio=info2["precio"])

            especia_nuevo.save()

            return render(request, "AppHealthy/inicio.html")
        
    else:
        nuevo_formulario2 = EspeciaFormulario
        
    return render(request, "AppHealthy/nueva_especia.html", {"mi_formu2": nuevo_formulario2})

def busqueda_especia(request):

    return render(request, "AppHealthy/busqueda_especias.html")

def resultado_buscarespecia(request):

    if request.method == "GET":

        nombre_buscado = request.GET["buscaespecia"]
        
        resultados_especias = Especias.objects.filter(nombre__icontains=nombre_buscado)
    
        return render(request, "AppHealthy/busqueda_especias.html", {"especia": resultados_especias})

    else:
        return render(request, "AppHealthy/busqueda_especias.html")
    