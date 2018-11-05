from django.db import models
from django.contrib import admin


class Marca(models.Model):

    nombre  =   models.CharField(max_length=60, verbose_name="Nombre")
    detalle  =   models.CharField(max_length=60, verbose_name="Detalle",help_text="Describa la marca")

    class Meta:
                verbose_name="Marca"
                verbose_name_plural="Marcas"
                ordering = ["-nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

class Categoria(models.Model):

    nombre  =   models.CharField(max_length=60)


    class Meta:
                verbose_name="Categoria"
                verbose_name_plural="Categorias"
                ordering = ["nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

    def __str__(self):

        return self.nombre


class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(verbose_name="Imagen",upload_to="prod",null=True,blank=True)
    fecha = models.DateField()
    detalle = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE,related_name="keymarca", help_text="Ingrese un numeros entero")
    categorias = models.ManyToManyField(Categoria,verbose_name="Categoria",related_name="keycategoria")

    class Meta:
                verbose_name="Producto"
                verbose_name_plural="Productos"
                ordering = ["-nombre"]

    def __str__(self):
        return self.nombre
