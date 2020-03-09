from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Vendor, Buyer, Invoice, CustomUser, Profile

admin.site.site_header = 'Facts Africa'

admin.site.register(Buyer)
admin.site.register(Profile)
admin.site.register(Vendor)
admin.site.register(Invoice)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']

admin.site.register(CustomUser, CustomUserAdmin)