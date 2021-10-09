from django.db import models
from .orders import Orders
from .products import Products

class Products_Orders(models.Model):
    id = models.AutoField(primary_key=True)    
    orders_id_fk = models.ForeignKey(Orders, related_name='orders_id.set()+', on_delete=models.CASCADE)
    orders_cantidad_fk = models.OneToOneField(Orders, to_field='cantidad', related_name='orders_cantidad.set()+', on_delete=models.CASCADE)
    products_id_fk = models.ForeignKey(Products, related_name='products_id.set()+', on_delete=models.CASCADE)
    products_codigo_fk = models.OneToOneField(Products, to_field='codigo', related_name='products_codigo.set()+', on_delete=models.CASCADE)
    products_precio_fk = models.OneToOneField(Products, to_field='precio', related_name='products_precio.set()+', on_delete=models.CASCADE)