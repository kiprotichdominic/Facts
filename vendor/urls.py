from django.urls import path

from .views import VendorView

urlpatterns = [
    path('vendor/', VendorView.as_view(), name ='vendor'),
]
