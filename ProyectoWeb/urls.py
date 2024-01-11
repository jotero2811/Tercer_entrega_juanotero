"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppHealthy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="Home"), 
    path("frutos/", agregar_frutos, name="Frutos"),
    path("semillas/", agregar_semilla, name="Semillas"),
    path("especias/", agregar_especias, name="Especias"),

    #URL para ingresar datos
    path("nuevofruto/", agregar_frutos, name="NuevoFruto"),
    path("nuevasemilla/", agregar_semilla, name="NuevaSemilla"),
    path("nuevaespecia/", agregar_especias, name="NuevaEspecia"),
    

    #URL para buscar datos
    path("buscarfrutoseco/", busqueda_frutoseco),
    path("buscarsemilla/", busqueda_semilla),
    path("buscarespecia", busqueda_especia),
    path("resultadofrutos/", resultado_buscarfrutoseco),
    path("resultadosemilla/", resultado_buscarsemilla),
    path("resultadoespecias/", resultado_buscarespecia),
]

