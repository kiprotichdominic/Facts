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
