from django.urls import path
from Optica.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('carga_marcos/', marcos),
    path('carga_cristales/', cristales),
    path('carga_liquidos/', liquidos),
]