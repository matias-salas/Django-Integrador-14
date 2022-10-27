from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

def media_directory_path(instance,filename):
    return 'productos/{0}'.format(filename)
        
class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to=media_directory_path, null=True, blank=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

