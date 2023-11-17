from django.urls import path
from Cuentas.views import login_usuario, registro, editar_perfil, EditarPassword, perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_usuario, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'Cuentas/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/editar/password', EditarPassword.as_view(), name='editar_password'),
]