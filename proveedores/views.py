from django.shortcuts import render
from django.views import generic

# Create your views here.
class ProveedorListView(generic.TemplateView):
    # model = Proveedor
    template_name = "proveedores/home.html"

