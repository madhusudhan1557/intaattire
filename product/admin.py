from django.contrib import admin
from product.models import ProductModel
# Register your models here.

class Products(admin.ModelAdmin):
    list_display = ['id', 'productname', 'productcode', 'price', 'image']

admin.site.register(ProductModel, Products)