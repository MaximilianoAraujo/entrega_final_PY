from django import forms

class CrearJuegoForm(forms.Form):
    nombre = forms.CharField (max_length=40)   
    genero = forms.CharField (max_length=40)
    precio = forms.IntegerField ()


class CrearConsolaForm(forms.Form):
    marca = forms.CharField (max_length=40)   
    modelo = forms.CharField (max_length=40)
    precio = forms.IntegerField ()


class CrearPerifericoForm(forms.Form):                      
    nombre = forms.CharField (max_length=40)   
    categoria = forms.CharField (max_length=40)
    descripcion = forms.CharField()
    precio = forms.IntegerField ()
