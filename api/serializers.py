from rest_framework import serializers
from accounts.models import Vendor, Buyer,Invoice, CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'email', 'company',)
        model = Vendor
        
        
class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'email', 'company',)
        model = Buyer
        
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name','status', 'buyer','status','invoice')
        model = Invoice

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'password')
        model = User