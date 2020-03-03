from django.shortcuts import render
from django.views.generic import TemplateView


class BuyerView(TemplateView):
    template_name = 'buyer/buyer.html'
