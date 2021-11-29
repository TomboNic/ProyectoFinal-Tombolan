from django.urls.conf import path
from .views import crear_basquet, crear_f1, crear_futbol, crear_voley, inicio, listaBasquet, listaF1, listaFutbol, listaVoley

urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("FanFutbol/", listaFutbol , name = "FanFutbol"),
    path("FanFutbol/crear/", crear_futbol , name = "CrearFanFutbol"),
    path("FanF1/", listaF1 , name = "FanF1"),
    path("FanF1/crear/", crear_f1 , name = "CrearFanF1"),
    path("FanBasquet/", listaBasquet , name = "FanBasquet"),
    path("FanBasquet/crear/", crear_basquet , name = "CrearFanBasquet"),
    path("FanVoley/", listaVoley , name = "FanVoley"),
    path("FanVoley/crear/", crear_voley , name = "CrearFanVoley"),
    ]