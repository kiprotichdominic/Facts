from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Products


class VendorView(ListView):
    template_name ='vendor/vendor.html'
    model = Products
    