from rest_framework import generics, viewsets
from accounts.models import Invoice, Vendor, Buyer
from rest_framework import generics, permissions
from .serializers import InvoiceSerializer, VendorSerializer, BuyerSerializer,UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer