from django.contrib import admin

# Register your models here.

from .models import Category,Product

# admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
