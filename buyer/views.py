from django.shortcuts import render
from django.views.generic import TemplateView


class BuyerView(TemplateView):
    template_name = 'buyer/buyer.html'

def orders(request,id):
    current_user=request.user
    product=Products.objects.get(id=id)
    ordered=Order(product_Name=product.name,price=product.price,buyer=current_user)
    ordered.save()
