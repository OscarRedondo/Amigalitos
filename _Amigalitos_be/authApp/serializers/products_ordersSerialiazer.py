from authApp.models.products_orders import Products_Orders
from rest_framework import serializers

class Products_OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products_Orders
        fields = ['id', 'orden_id_fk', 'orden_cantidad_fk', 'producto_id_fk', 'producto_codigo_fk', 'producto_precio_fk']