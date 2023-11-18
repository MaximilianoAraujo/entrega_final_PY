from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from Cuentas.forms import FormRegistro, FormEditarPerfil
from Cuentas.models import MasDatos
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def login_usuario(request):
    if request.method == 'POST':
        formulario_login = AuthenticationForm(request, data = request.POST)
        if formulario_login.is_valid():
            usuario = formulario_login.cleaned_data.get('username')
            contrasenia = formulario_login.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contrasenia)

            login(request, user)

            MasDatos.objects.get_or_create(user = request.user)

            return redirect('inicio')
        else:
            return render(request, 'Cuentas/login.html', {'formulario_login':formulario_login})

    formulario_login = AuthenticationForm()
    return render(request, 'Cuentas/login.html', {'formulario_login':formulario_login})

def registro(request):
    formulario_registro = FormRegistro()

    if request.method == 'POST':
        formulario_registro = FormRegistro(request.POST)
        if formulario_registro.is_valid():
            
            formulario_registro.save()

            return redirect('login')

    return render(request, 'Cuentas/registro.html', {'formulario_registro': formulario_registro})

def perfil(request):

    mas_datos = None
    mas_datos = request.user.masdatos

    return render(request, 'cuentas/perfil.html', {'mas_datos': mas_datos})


def editar_perfil(request):
    mas_datos = request.user.masdatos

    formulario_editar = FormEditarPerfil(instance = request.user, initial = {'biografia': mas_datos.biografia, 'avatar': mas_datos.avatar})

    if request.method == 'POST':
        formulario_editar = FormEditarPerfil(request.POST, request.FILES, instance = request.user)

        if formulario_editar.is_valid():
            nueva_biografia = formulario_editar.cleaned_data.get('biografia')
            nuevo_avatar = formulario_editar.cleaned_data.get('avatar')

            if nueva_biografia:
                mas_datos.biografia = nueva_biografia
            if nuevo_avatar:
                mas_datos.avatar = nuevo_avatar

            mas_datos.save()
            formulario_editar.save()

            return redirect('perfil')
    
    return render(request, 'cuentas/editar_perfil.html', {'formulario_editar':formulario_editar})

class EditarPassword(PasswordChangeView):
    template_name = 'cuentas/editar_password.html'
    success_url = reverse_lazy('perfil')