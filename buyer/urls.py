from django.urls import path

from .views import HomeView
from . import views

urlpatterns = [
    path('', views.HomeView, name ='buyer'),
]
