from authApp.models.products import Products
from rest_framework import serializers

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'nombre', 'precio', 'descripcion', 'miniatura', 'categoria', 'vencimiento', 'stock', 'imagenes', 'categoria']