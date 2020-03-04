from django.urls import path

from .views import BuyerView

urlpatterns = [
    path('', BuyerView.as_view(), name ='buyer'),
]
