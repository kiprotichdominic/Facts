from django.db import models
from datetime import datetime



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