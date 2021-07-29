from django.contrib import admin
from .models import Product

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit', 'status', 'user', 'date_created', 'updated']

admin.site.register(Product, AdminProduct)