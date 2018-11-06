from django import forms

from .models import Marca, Categoria, Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = [
            'nombre',
            'imagen',
            'fecha',
            'detalle',
            'marca',
            'categorias',
        ]
        labels = {
            'nombre': 'Nombre',
            'imagen' : 'Imagen',
            'fecha': 'Fecha',
            'detalle': 'Detalle',
            'marca': 'Marca',
            'categorias': 'Categoria De Producto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'detalle': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'categorias': forms.CheckboxSelectMultiple(),
        }

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = [
            'nombre',
            'detalle',
        ]

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = [
            'nombre',
        ]
