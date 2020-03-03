from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=charfield(max_lenth=20)
    email=models.EmailField()
    phone=models.IntegerField()

class Categories(models.Model):

    PRODUCT_CHOICES = (
        ("agriculture", "agriculture"),
        ("electronics", "electronics"),
        ("cars", "cars"),
        ("utensils", "utensils"),

    )


    choice=models.charfield( chioces= PRODUCT_CHOICES)


class Products(models.Model):
    product_Name=models.charfield(max_lenth=20)
    category=Foreignkey(Category)
    category=Foreignkey(User)
    quantity=models.IntegerField()
    location = models.CharField(max_length=30, blank=True)
    date_Posted= models.DateField(null=True, blank=True)
