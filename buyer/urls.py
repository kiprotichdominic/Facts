from django.urls import path

from .views import BuyerView

urlpatterns = [
    path('buyer/', BuyerView.as_view(), name ='buyer'),
    path(r'render/pdf/(?P<pk>[0-9]+)/$', Pdf.as_view())
]
