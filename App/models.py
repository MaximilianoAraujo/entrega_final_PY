from django.db import models

class Juego(models.Model):                      
    nombre = models.CharField (max_length=40)   
    genero = models.CharField (max_length=40)
    precio = models.IntegerField ()

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.genero}'
    

class Consola(models.Model):                      
    marca = models.CharField (max_length=40)   
    modelo = models.CharField (max_length=40)
    precio = models.IntegerField ()

    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo}'
    

class Periferico(models.Model):                      
    nombre = models.CharField (max_length=40)   
    categoria = models.CharField (max_length=40)
    descripcion = models.TextField()
    precio = models.IntegerField ()

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.categoria}'