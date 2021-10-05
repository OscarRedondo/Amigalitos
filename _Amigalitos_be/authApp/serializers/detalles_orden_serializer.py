from authApp.models.detalles_orden import Detalles_Orden
from rest_framework import serializers

class Detalles_Orden_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Detalles_Orden
        fields = ['detallesOrden_id', 'orden_id_fk', 'orden_cantidad_fk', 'orden_cantidad_fk', 'producto_id_fk',
                    'producto_codigo_fk', 'producto_precio_fk']