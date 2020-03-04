from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()
<<<<<<< HEAD



=======
>>>>>>> d42a3672f6191090dd6727ae013cfdd11be03b29
class Order(models.Model):
    '''
    The Order model represents a customer order. It includes a
    ManyToManyField of products the customer is ordering and stores
    the date and total price information.
    '''
    customer = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
<<<<<<< HEAD
    status_code = models.For
    eignKey('StatusCode', on_delete=models.CASCADE)
=======
    status_code = models.ForeignKey('StatusCode', on_delete=models.CASCADE)
>>>>>>> d42a3672f6191090dd6727ae013cfdd11be03b29
    date_placed = models.DateTimeField(default=datetime.now)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    comments = models.TextField(blank=True)
    products = models.ManyToManyField('vendor.Products')
<<<<<<< HEAD

=======
>>>>>>> d42a3672f6191090dd6727ae013cfdd11be03b29
class StatusCode(models.Model):
    '''
    The StatusCode model represents the status of an order in the
    system.
    '''
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=300)
<<<<<<< HEAD
    description = models.TextField()
=======
    description = models.TextField()
>>>>>>> d42a3672f6191090dd6727ae013cfdd11be03b29
