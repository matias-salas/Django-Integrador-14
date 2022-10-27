from tkinter import Widget
from django import forms
from .models import  Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'imagen']
        widgets = {
            # 'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            # 'precio': forms.TextInput(attrs={'class': 'form-control'}),
            # 'stock': forms.TextInput(attrs={'class': 'form-control'}),
            # 'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            # 'categoria': forms.Select(attrs={'class': 'form-control'}),
            # 'proveedor': forms.Select(attrs={'class': 'form-control'}),
        }


