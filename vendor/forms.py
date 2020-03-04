from django.forms import ModelForm
from .models import Products
class ProductsForm(ModelForm):
     class Meta:
       model = Products
       fields = ['product_Name', 'category', 'quantity', 'location','date_Posted']
