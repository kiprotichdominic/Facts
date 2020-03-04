from django.db import models
<<<<<<< HEAD
#from django.contrib.auth.models import User
from vendor/models import Product

class buyer(models.Model):
    # user=OneToOneField(User)
    email=models.EmailField()


    def __str__(self):
        return self.user.username

class Order(models.Model):
    product_Name=models.CharField(max_length=200)
    Price=models.DecimalField(max_digits=5, decimal_places=2)
    buyer=models.ForeignKey(buyer,on_delete=models.CASCADE,related_name='orders')
    def __str__(self):
        return self.product_Name
=======
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()
class Order(models.Model):
    '''
    The Order model represents a customer order. It includes a
    ManyToManyField of products the customer is ordering and stores
    the date and total price information.
    '''
    customer = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    status_code = models.ForeignKey('StatusCode', on_delete=models.CASCADE)
    date_placed = models.DateTimeField(default=datetime.now)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    comments = models.TextField(blank=True)
    products = models.ManyToManyField('vendor.Products')
class StatusCode(models.Model):
    '''
    The StatusCode model represents the status of an order in the
    system.
    '''
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=300)
    description = models.TextField()
>>>>>>> d42a3672f6191090dd6727ae013cfdd11be03b29
