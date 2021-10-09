from authApp.models.orders import Orders
from rest_framework import serializers

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'cantidad', 'fechaPedido', 'estadoPedido', 'usuario_correo_fk', 'usuario_dirFacturacion_fk', 'usuario_dirEntrega_fk']