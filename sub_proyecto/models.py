from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.
class Paginas(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Image",null=True)
    Descripcion = models.TextField(verbose_name="Descripción",null=True)
    valor = models.IntegerField(verbose_name="Valor")
    url = models.CharField(max_length=100)

    def __str__(self) :
        fila = "Titulo: " + self.titulo +  " - " + "Descripción: " + self.Descripcion
        return fila
    
    def delete(self, using= None, keep_parents = False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=100, verbose_name="Rut")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    password = models.CharField(max_length=100, verbose_name="Password")
    rol = models.IntegerField(verbose_name="Rol")

class UserNueva(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=13, verbose_name="Rut")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    password = models.CharField(max_length=100, verbose_name="Password")
    rol = models.IntegerField(verbose_name="Rol")

    def __str__(self) :
        fila = "Rut: " + self.rut +  " - " + "Nombre: " + self.nombre + " - " + "Apellido: " + self.apellido
        return fila