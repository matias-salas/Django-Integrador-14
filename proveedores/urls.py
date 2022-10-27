from django.urls import path

from .views import (
    ProductoNuevo,
    ProductoEditar,
    ProductoListar,
    HomeListView,
)
app_name = 'proveedores'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('nuevo-producto/', ProductoNuevo.as_view(), name='nuevo-producto'),
    path('editar-producto/<int:pk>/', ProductoEditar.as_view(), name='editar-producto'),
    path('listado-producto/', ProductoListar.as_view(), name='listado-producto'),
]