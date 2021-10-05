from django.db import models

class Productos(models.Model):
    producto_id = models.AutoField(primary_key=True)
    producto_nombre = models.CharField(default='-', max_length=40)
    producto_precio = models.IntegerField(default=0)
    producto_descripcion = models.DateTimeField()
    producto_miniatura = models.CharField(default='-', max_length=40)
    producto_categoria = models.CharField(default='-', max_length=40)
    producto_vencimiento = models.DateTimeField()
    producto_stock = models.IntegerField(default=0)
    producto_imagenes = models.CharField(default='-', max_length=40)