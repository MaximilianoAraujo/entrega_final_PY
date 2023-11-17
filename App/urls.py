from django.urls import path
from App.views import juegos, inicio, crear_juego, crear_consola, crear_periferico, EliminarJuego, actualizar_juego, about_me, DetalleJuego

urlpatterns = [
    path('', inicio, name='inicio'),
    path('juegos/', juegos, name='juegos'),
    path('juegos/crear/', crear_juego, name='crear_juego'),
    path('juegos/<int:pk>/eliminar/', EliminarJuego.as_view(), name='eliminar_juego'),
    path('juegos/<int:juego_id>/actualizar/', actualizar_juego, name='actualizar_juego'),
    path('juegos/<int:pk>/detalle/', DetalleJuego.as_view(), name='detalle_juego'),
    path('consolas/crear/', crear_consola, name='crear_consola'),
    path('perifericos/crear/', crear_periferico, name='crear_periferico'),
    path('sobre_mi/', about_me, name='about_me'),
]