from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import *

# Create your views here.

class ProductoNuevo(generic.CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'proveedores/crear_producto.html'
    success_url = reverse_lazy('proveedores:nuevo-producto')

# OTRA FORMA DE HACERLO
# class ProductoNuevo(generic.View):
#     def get(self, request):
#         form = ProductoForm()
#         print("Estoy en el get")
#         return render(request, 'proveedores/crear_producto.html', {'form': form})

#     def post(self, request):
#         form = ProductoForm(request.POST, request.FILES)
#         print("Estoy en el post")

#         if form.is_valid():
#             form.save()
#             return render(request, 'proveedores/crear_producto.html', {'form': form})
#         else:
#             return render(request, 'proveedores/crear_producto.html', {'form': form})

class ProductoListar(generic.ListView):
    model = Producto
    template_name = 'proveedores/producto_list.html'
    context_object_name = 'productos' 
    
    def get_queryset(self):
        return Producto.objects.all()

    
class ProductoEditar(generic.UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'proveedores/editar_producto.html'
    # success_url = reverse_lazy('proveedores:nuevo-producto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        return context


class HomeListView(generic.ListView):
    model = Producto
    template_name = 'proveedores/home.html'
    context_object_name = 'productos' 
    
    def get_queryset(self):
        return Producto.objects.all()