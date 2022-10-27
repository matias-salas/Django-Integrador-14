from django.urls import path

from .views import (
    ProveedorListView,
)
app_name = 'proveedores'

urlpatterns = [
    path('', ProveedorListView.as_view(), name="index"),
]