from django.urls import path
from App.views import juegos, inicio, crear_juego, crear_consola, crear_periferico

urlpatterns = [
    path('', inicio, name='inicio'),
    path('juegos/busqueda/', juegos, name='juegos'),
    path('juegos/crear/', crear_juego, name='crear_juego'),
    path('consolas/crear/', crear_consola, name='crear_consola'),
    path('perifericos/crear/', crear_periferico, name='crear_periferico'),
]