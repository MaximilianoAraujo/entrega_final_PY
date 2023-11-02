from django.shortcuts import render, redirect
from App.models import Juego, Consola, Periferico
from App.forms import CrearJuegoForm, CrearConsolaForm, CrearPerifericoForm

def inicio(request) :
    return render(request,'App/inicio.html', {})


def juegos(request) :

    juego_buscado = request.GET.get('nombre')

    if juego_buscado:
        lista_juegos = Juego.objects.filter(nombre__icontains = juego_buscado)
    else:
        lista_juegos = Juego.objects.all()

    return render(request,'App/juegos.html', {'lista_juegos': lista_juegos})


def crear_juego(request):

    if request.method == 'POST':
        formulario_juego = CrearJuegoForm(request.POST)

        if formulario_juego.is_valid():
            info = formulario_juego.cleaned_data

            nombre = info.get('nombre')
            genero = info.get('genero')
            precio = info.get('precio')

            juego = Juego(nombre = nombre, genero = genero, precio = precio)
            juego.save()

            return redirect('juegos')
        
        else:
            return render(request,'App/crear_juego.html', {'formulario_juego': formulario_juego})

    formulario_juego = CrearJuegoForm()
    return render(request,'App/crear_juego.html', {'formulario_juego': formulario_juego})


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

