from django.shortcuts import render, redirect
from App.models import Juego, Consola, Periferico
from App.forms import CrearJuegoForm, CrearConsolaForm, CrearPerifericoForm, ActualizarJuegoForm
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def inicio(request) :
    return render(request,'App/inicio.html', {})


def juegos(request) :

    juego_buscado = request.GET.get('nombre')

    if juego_buscado:
        lista_juegos = Juego.objects.filter(nombre__icontains = juego_buscado)
    else:
        lista_juegos = Juego.objects.all()

    return render(request,'App/juegos.html', {'lista_juegos': lista_juegos})


@login_required
def crear_juego(request):

    if request.method == 'POST':
        formulario_juego = CrearJuegoForm(request.POST, request.FILES)

        if formulario_juego.is_valid():
            info = formulario_juego.cleaned_data

            nombre = info.get('nombre')
            genero = info.get('genero')
            descripcion = info.get('descripcion')
            precio = info.get('precio')
            fecha_lanzamiento = info.get('fecha_lanzamiento')
            portada = info.get('portada')

            juego = Juego(nombre=nombre, genero=genero, descripcion=descripcion, precio=precio, fecha_lanzamiento=fecha_lanzamiento, portada=portada)
            juego.save()

            return redirect('juegos')
        
        else:
            return render(request,'App/crear_juego.html', {'formulario_juego': formulario_juego})

    formulario_juego = CrearJuegoForm()
    return render(request,'App/crear_juego.html', {'formulario_juego': formulario_juego})


class EliminarJuego(LoginRequiredMixin, DeleteView):
    model = Juego
    template_name = "App/eliminar_juego.html"
    success_url = reverse_lazy('juegos')


@login_required
def actualizar_juego(request, juego_id):
    juego_a_actualizar = Juego.objects.get(id=juego_id)

    if request.method == 'POST':
        formulario_actualizar = ActualizarJuegoForm(request.POST, request.FILES, instance=juego_a_actualizar)

        if formulario_actualizar.is_valid():
            formulario_actualizar.save()
            return redirect('juegos')
        else:
            return render(request, 'App/actualizar_juego.html', {'formulario_actualizar': formulario_actualizar})

    formulario_actualizar = ActualizarJuegoForm(instance=juego_a_actualizar)
    return render(request, 'App/actualizar_juego.html', {'formulario_actualizar': formulario_actualizar})


class DetalleJuego(DetailView):
    model = Juego
    template_name = "App/detalle_juego.html"


@login_required
def crear_consola(request):

    if request.method == 'POST':
        formulario_consola = CrearConsolaForm(request.POST)

        if formulario_consola.is_valid():
            info = formulario_consola.cleaned_data

            marca = info.get('marca')
            modelo = info.get('modelo')
            precio = info.get('precio')

            consola = Consola(marca = marca, modelo = modelo, precio = precio)
            consola.save()
        
        else:
            return render(request,'App/crear_consola.html', {'formulario_consola': formulario_consola})

    formulario_consola = CrearConsolaForm()
    return render(request,'App/crear_consola.html', {'formulario_consola': formulario_consola})


def crear_periferico(request):

    if request.method == 'POST':
        formulario_periferico = CrearPerifericoForm(request.POST)

        if formulario_periferico.is_valid():
            info = formulario_periferico.cleaned_data

            nombre = info.get('nombre')
            categoria = info.get('categoria')
            descripcion = info.get('descripcion')
            precio = info.get('precio')

            periferico = Periferico(nombre = nombre, categoria = categoria, descripcion = descripcion, precio = precio)
            periferico.save()
        
        else:
            return render(request,'App/crear_periferico.html', {'formulario_periferico': formulario_periferico})

    formulario_periferico = CrearPerifericoForm()
    return render(request,'App/crear_periferico.html', {'formulario_periferico': formulario_periferico})


def about_me(request):
    return render(request, 'App/about_me.html')