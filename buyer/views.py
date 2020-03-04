from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import Render

class BuyerView(TemplateView):
<<<<<<< HEAD
    template_name = 'buyer/buyer.html'

def orders(request,id):
    current_user=request.user
    product=Products.objects.get(id=id)
    ordered=Order(product_Name=product.name,price=product.price,buyer=current_user)


class Pdf(View):

    def get(self, request,id):
        current_user=request.user
        product=Products.objects.get(id=id)
        ordered=Order(product_Name=product.name,price=product.price,buyer=current_user)
        today = timezone.now()
        ordered.save()
        params = {
            'today': today,
            'orders': ordered,
            'request': request
        }
        return Render.render('invoice.html', params)
=======
    template_name = 'buyer/index.html'
>>>>>>> d42a3672f6191090dd6727ae013cfdd11be03b29
