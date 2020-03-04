from django.db import models
#from django.contrib.auth.models import User

class buyer(models.Model):
    # user=OneToOneField(User)
    email=models.EmailField()


    def __str__(self):
        return self.user.username

class Order(models.Model):
    product_Name=models.CharField(max_length=200)
    Price=models.DecimalField(max_digits=5, decimal_places=2)
    orders=models.ForeignKey(buyer,on_delete=models.CASCADE,related_name='orders')
    def __str__(self):
        return self.product_Name
