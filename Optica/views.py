from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from Optica.models import *
from Optica.templates import *
from Optica.forms import *

# Create your views here.

def inicio(request):
    return render(request,"Optica/base.html")

#def marcos(request):
 #   return render(request,"Optica/carga_marcos.html")

def crear_marcos(request):
    if request.method == "POST":
        formulario = formulario_Marcos(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            marco = Marcos(nombre=data["nombre"], marca=data["marca"], precio=data["precio"])
            marco.save()

    formulario = formulario_Marcos()
    contexto = {"formulario": formulario}
    return render(request, "Optica/carga_marcos.html", contexto)

def buscar_marcos(request):
    return render(request, "Optica/busqueda_marcos.html")

def resultados_marcos(request):
    nombre_marco = request.GET["nombre_marco"]

    marcos = Marcos.objects.filter(nombre__icontains=nombre_marco)
    return render(request, "Optica/resultados_busqueda_marcos.html", {"marcos": marcos})





#def liquidos(request):
 #   return render(request,"Optica/carga_liquidos.html")

def crear_liquidos(request):
    if request.method == "POST":
        formulario = formulario_liquidos(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            liquido = Liquidos(nombre=data["nombre"], marca=data["marca"], precio=data["precio"])
            liquido.save()


    formulario = formulario_liquidos()
    contexto = {"formulario": formulario}
    return render(request, "Optica/carga_liquidos.html", contexto)

def buscar_liquidos(request):
    return render(request, "Optica/busqueda_liquidos.html")

def resultados_liquidos(request):
    nombre_liquido = request.GET["nombre_liquido"]

    liquidos = Liquidos.objects.filter(nombre__icontains=nombre_liquido)
    return render(request, "Optica/resultados_busqueda_liquidos.html", {"liquidos": liquidos})







#def cristales(request):
 #   return render(request,"Optica/carga_cristales.html")

def crear_cristales(request):
    if request.method == "POST":
        formulario = formulario_cristales(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            cristales = Cristales(nombre=data["nombre"], precio=data["precio"])
            cristales.save()


    formulario = formulario_cristales()
    contexto = {"formulario": formulario}
    return render(request,"Optica/carga_cristales.html", contexto)

def buscar_cristal(request):
    return render(request, "Optica/busqueda_cristales.html")

def resultados_cristales(request):
    nombre_cristal = request.GET["nombre_cristal"]

    cristales = Cristales.objects.filter(nombre__icontains=nombre_cristal)
    return render(request, "Optica/resultados_busqueda_cristales.html", {"cristales": cristales})