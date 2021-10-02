from rest_framework import serializers
from authApp.models.user import User
from authApp.models.account import Account
from authApp.serializers.account_serializer import Account_Serializer

class User_Serializer(serializers.Model_Serializer):
    account = Account_Serializer()
    class Meta:
        model = User
        fields = ['usuario_id', 'usuario_username', 'usuario_contraseña', 'usuario_nombre', 'usuario_correo', 'usuario_dirFacturacion', 'usuario_dirEntrega',
            'usuario_ciudad', 'usuario_telefono']
    
    def create(self, validated_data):
        account_data = validated_data.pop('account')
        user_instance = User.objects.create(**validated_data)
        Account.objects.create(user=user_instance, **account_data)
        return user_instance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'usuario_id': user.id,  
            'usuario_username': user.username,
            'usuario_nombre': user.name,
            'usuario_correo': user.email,            
        }