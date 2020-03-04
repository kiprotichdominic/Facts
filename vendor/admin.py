from django.contrib import admin

from .models import Category, Products,Vendor

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Vendor)