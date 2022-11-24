from django.urls import path
from Optica.views import *


urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('carga_marcos/', crear_marcos, name="marcos"),
    path('carga_cristales/', crear_cristales, name="cristales"),
    path('carga_liquidos/', crear_liquidos, name="liquidos"),

    path('cristales/buscar/', buscar_cristal, name="Optica-cristales-buscar"),
    path('cristales/buscar/resultados/',resultados_cristales , name="Optica-cristales-buscar-resultados"),

    path('marcos/buscar/', buscar_marcos , name="Optica-marcos-buscar"),
    path('marcos/buscar/resultados/', resultados_marcos , name="Optica-marcos-buscar-resultados"),

    path('liquidos/buscar/', buscar_liquidos , name="Optica-liquidos-buscar"),
    path('liquidos/buscar/resultados/', resultados_liquidos , name="Optica-liquidos-buscar-resultados"),
]