from rest_framework import serializers
from .models import Bank, Provider

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('name' , )

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('name', 'nit', 'contact_name', 'contact_phone', 'bank', 'account_bank', )