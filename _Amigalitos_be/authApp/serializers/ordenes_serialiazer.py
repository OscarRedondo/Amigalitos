from authApp.models.ordenes import Ordenes
from rest_framework import serializers

class Ordenes_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes
        fields = ['orden_id', 'orden_cantidad', 'orden_fechaPedido', 'orden_estadoPedido', 'usuario_correo',
                    'usuario_dirFacturacion', 'usuario_dirEntrega']