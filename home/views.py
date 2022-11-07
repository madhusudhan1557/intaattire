from django.shortcuts import render
from product.models import ProductModel
# Create your views here.
def homepage(request):
    products = ProductModel.objects.all()
    return render(request, 'home.html', {"products" : products})

def aboutpage(request):
    return render(request, 'about.html')

def shop_page(request):
    products = ProductModel.objects.all()
    return render(request, 'shop.html', {"products" : products})
    
def order_form(request):
     return render(request, 'form.html')