from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from Optica.models import *
from Optica.templates import *

# Create your views here.

def inicio(request):
    return render(request,"Optica/base.html")

def marcos(request):
    return render(request,"Optica/carga_marcos.html")

def liquidos(request):
    return render(request,"Optica/carga_liquidos.html")

def cristales(request):
    return render(request,"Optica/carga_cristales.html")