from django.urls import path

from .views import BuyerView

urlpatterns = [
<<<<<<< HEAD
    path('buyer/', BuyerView.as_view(), name ='buyer'),
    path(r'render/pdf/(?P<pk>[0-9]+)/$', Pdf.as_view())
=======
    path('', BuyerView.as_view(), name ='buyer'),
>>>>>>> d42a3672f6191090dd6727ae013cfdd11be03b29
]
