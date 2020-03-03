from django.shortcuts import render
from django.views.generic import TemplateView


class VendorView(TemplateView):
    template_name ='vendor/vendor.html'