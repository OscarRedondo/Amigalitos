from django.db import models
from authApp.models.ordenes import Ordenes
from authApp.models.productos import Productos

class Detalles_Orden(models.Model):
    detallesOrden_id = models.AutoField(primary_key=True)
    #orden_id_fk = models.ForeignKey(Ordenes, related_name='orden_id', on_delete=models.CASCADE)
    #orden_cantidad_fk = models.ForeignKey(Ordenes, related_name='orden_cantidad', on_delete=models.CASCADE)
    #orden_cantidad_fk = models.ForeignKey(Ordenes, related_name='orden_cantidad', on_delete=models.CASCADE)
    #producto_id_fk = models.ForeignKey(Productos, related_name='producto_id', on_delete=models.CASCADE)
    producto_codigo_fk = models.ForeignKey(Productos, related_name='producto_codigo', on_delete=models.CASCADE)
    #producto_precio_fk = models.ForeignKey(Productos, related_name='producto_precio', on_delete=models.CASCADE)