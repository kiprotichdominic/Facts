from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser


from .models import Invoice


class InvoiceForm(ModelForm):
	class Meta:
		model = Invoice
		fields = ('name', 'buyer','invoice')


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')