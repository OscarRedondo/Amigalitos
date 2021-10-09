from django.db import models

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(default='-', max_length=40, unique=True)
    nombre = models.CharField(default='-', max_length=40)
    precio = models.IntegerField(default=0, unique=True)
    descripcion = models.CharField(default='-', max_length=40)
    miniatura = models.CharField(default='-', max_length=40)
    categoria = models.CharField(default='-', max_length=40)
    vencimiento = models.DateTimeField()
    stock = models.IntegerField(default=0)
    imagenes = models.CharField(default='-', max_length=40)
    categoria = models.CharField(default='-', max_length=40)