from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=charfield(max_lenth=20)
    email=models.EmailField()
    phone=models.IntegerField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Categories(models.Model):

    PRODUCT_CHOICES = (
        ("agriculture", "agriculture"),
        ("electronics", "electronics"),
        ("cars", "cars"),
        ("utensils", "utensils"),

    )


    choices=models.charfield( chioces= PRODUCT_CHOICES)


class Products(models.Model):
    product_Name=models.charfield(max_lenth=20)
    category=Foreignkey(Category)
    category=Foreignkey(User)
    quantity=models.IntegerField()
    location = models.CharField(max_length=30, blank=True)
    date_Posted= models.DateField(null=True, blank=True)
