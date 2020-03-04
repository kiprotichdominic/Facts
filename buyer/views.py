from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from vendor.models import Category,Vendor,Products

def HomeView(request):
    category = Category.objects.all()
    vendor = Vendor.objects.all()
    product = Products.objects.all()

    mydict = {'category':category, 'vendor':vendor, 'product':product}
    return render(request, 'buyer/index.html', context=mydict)
    