from authApp.models.productos import Productos
from rest_framework import serializers

class Productos_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['producto_id', 'producto_nombre' 'producto_precio', 'producto_descripcion',
                    'producto_miniatura', 'producto_categoria', 'producto_vencimiento', 'producto_stock'
                    'producto_imagenes']