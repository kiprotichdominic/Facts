from django.urls import path

from .views import HomeView
from . import views

urlpatterns = [
    path(r'render/pdf/(?P<pk>[0-9]+)/$', Pdf.as_view())
    path('', BuyerView.as_view(), name ='buyer'),
]
