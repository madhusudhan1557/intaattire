from django.shortcuts import render
from product.models import ProductModel
from banners.models import BannerModel
# Create your views here.
def homepage(request):
    products = ProductModel.objects.all()
    banners = BannerModel.objects.all()
    return render(request, 'home.html', {"products" : products, 'banners' : banners})

def aboutpage(request):
    banner = BannerModel.objects.first()
    return render(request, 'about.html', {"banner" : banner})

def shop_page(request):
    products = ProductModel.objects.all()
    banner = BannerModel.objects.last()
    return render(request, 'shop.html', {"products" : products, "banner" : banner})
    
def order_form(request):
     return render(request, 'form.html')

def contactpage(request):
    return render(request, 'contact.html')