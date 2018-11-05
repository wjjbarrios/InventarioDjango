from django.contrib import admin
from productos.models import Marca, Categoria, Producto

#Registramos nuestras clases principales.
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Producto)
