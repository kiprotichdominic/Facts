from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=150)
    image = models.ImageField()
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    vendor = models.ForeignKey('Vendor',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.name

# class Order(models.Model):
#         '''
#     The Order model represents a customer order. It includes a
#     ManyToManyField of products the customer is ordering and stores
#     the date and total price information.
#     '''
#     # customer = models.ForeignKey(User, blank=True, null=True)
#     status_code = models.ForeignKey('StatusCode')
#     date_placed = models.DateTimeField()
#     total_price = models.DecimalField(max_digits=7, decimal_places=2)
#     comments = models.TextField(blank=True)
#     products = models.ManyToManyField(Product,
#     through='ProductInOrder')

# class StatusCode(models.Model):
#         '''
#     The StatusCode model represents the status of an order in the
#     system.
#     '''
#     short_name = models.CharField(max_length=10)
#     name = models.CharField(max_length=300)
#     description = models.TextField()