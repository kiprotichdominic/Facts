from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image



class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.email

class Buyer(models.Model):
	name = models.CharField(max_length=200, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	# email = models.CharField(max_length=200, null=True)
	# company = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	# vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE)

	def __str__(self):
		return self.name
    
	@property
	def invoices(self):
		invoice_count = self.invoice_set.all().count()
		return str(invoice_count)


class Vendor(models.Model):
    name = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    # email = models.CharField(max_length=200, null=True)
    # company = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
       return self.name


class Invoice(models.Model):
	STATUS = (
			('Approve', 'Approve'),
			('Decline', 'Decline'),
			('Pending', 'Pending'),
			)
	# buyer = models.ForeignKey(Buyer, on_delete= models.SET_NULL, null=True)
	name = models.CharField(max_length=200, null=True)
	buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
	# vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
	invoice = models.FileField(upload_to='documents/')
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS, default='Pending')
 
	def __str__(self):
		return self.name


class Profile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
		    output_size = (300, 300)
		    img.thumbnail(output_size)
		    img.save(self.image.path)
            