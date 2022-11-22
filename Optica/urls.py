from django.urls import path
from Optica.views import *

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('carga_marcos/', marcos, name="marcos"),
    path('carga_cristales/', cristales, name="cristales"),
    path('carga_liquidos/', liquidos, name="liquidos"),
]