from authApp.models.account import Account
from rest_framework import serializers

class Account_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['balance', 'lastChangeDate', 'isActive']