from django import forms
from ckeditor.fields import RichTextFormField
from App.models import Juego

class CrearJuegoForm(forms.Form):
    nombre = forms.CharField (max_length=40)   
    genero = forms.CharField (max_length=40)
    descripcion = RichTextFormField()
    precio = forms.IntegerField ()
    fecha_lanzamiento = forms.DateField()
    portada = forms.ImageField()

class ActualizarJuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['nombre', 'genero', 'precio', 'descripcion', 'fecha_lanzamiento', 'portada']

class CrearConsolaForm(forms.Form):
    marca = forms.CharField (max_length=40)   
    modelo = forms.CharField (max_length=40)
    precio = forms.IntegerField ()

class CrearPerifericoForm(forms.Form):                      
    nombre = forms.CharField (max_length=40)   
    categoria = forms.CharField (max_length=40)
    descripcion = forms.CharField()
    precio = forms.IntegerField ()