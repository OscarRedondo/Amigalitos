from rest_framework import serializers
from authApp.models.usuarios import Usuarios
from authApp.models.account import Account
from authApp.serializers.account_serializer import Account_Serializer

class Usuarios_Serializer(serializers.Model_Serializer):
    account = Account_Serializer()
    class Meta:
        model = Usuarios
        fields = ['usuario_id', 'username', 'usuario_contraseña', 'usuario_nombre', 'usuario_correo', 'usuario_dirFacturacion', 'usuario_dirEntrega',
            'usuario_ciudad', 'usuario_telefono']
    
    def create(self, validated_data):
        account_data = validated_data.pop('account')
        user_instance = Usuarios.objects.create(**validated_data)
        Account.objects.create(user=user_instance, **account_data)
        return user_instance

    def to_representation(self, obj):
        user = Usuarios.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'usuario_id': user.usuario_id,  
            'username': user.username,
            'usuario_nombre': user.usuario_nombre,
            'usuario_email': user.usuario_email
        }