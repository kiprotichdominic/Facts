from django.shortcuts import render
from django.views.generic import TemplateView,ListView, View
from vendor.models import Category,Vendor,Products
from django.utils import timezone
from .models import *
from .render import Render

def HomeView(request):
    category = Category.objects.all()
    vendor = Vendor.objects.all()
    product = Products.objects.all()
    mydict = {'category':category, 'vendor':vendor, 'product':product}
    return render(request, 'buyer/index.html', context=mydict)

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
    template_name = 'buyer/index.html'
