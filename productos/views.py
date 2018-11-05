from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ProductoForm
from productos.models import Producto, Categoria, Marca
from django.contrib.auth.decorators import login_required


@login_required
def lista_productos(request):
    producto = Producto.objects.all()
    return render(request, 'productos/listaproducto.html', {'producto': producto})

def detalle_producto(request, pk):
     producto = get_object_or_404(Producto,pk=pk)
     categoria = Categoria.objects.all()
     marca = Marca.objects.all()
     return render(request,"productos/detalle_producto.html",{'producto':producto,'categoria':categoria,'marca':marca})

def Eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('lista_productos')

def producto_nuevo(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_productos')
            messages.add_message(request, messages.SUCCESS, 'producto Guardada Exitosamente')
    else:
        formulario = ProductoForm()
    return render(request, 'productos/producto_editar.html', {'formulario': formulario})

def Editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            producto = formulario.save()
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)

    else:
        formulario = ProductoForm(instance=producto)
    return render(request, 'productos/producto_editar.html', {'formulario': formulario})
