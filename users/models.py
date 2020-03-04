<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
=======
>>>>>>> 36c248c88e02e5d5d241a6e74edfdbb51928a90e
