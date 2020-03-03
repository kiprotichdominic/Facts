from django.urls import path

from .views import BuyerView

urlpatterns = [
    path('buyer/', BuyerView.as_view(), name ='buyer'),
]
