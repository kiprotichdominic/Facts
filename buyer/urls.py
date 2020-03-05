from django.urls import path

from . import views
from buyer.views import Pdf

urlpatterns = [
    path('render/invoice/<int:id>/', Pdf.as_view()),
    path('', views.HomeView, name ='buyer'),
]
