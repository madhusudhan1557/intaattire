from django.shortcuts import render
from product.models import ProductModel
from banners.models import BannerModel
from orders.models import OrderModel
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

def sendOrder(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        productname = request.POST.get('productname')
        productcode = request.POST.get('productcode')
        location = request.POST.get('location')
        paymentcode = request.POST.get('paymentcode')
        message = request.POST.get('message')
        remarks = request.POST.get('remarks')
        OrderModel.objects.create(fullname=fullname, email=email, phone=phone, productname=productname,productcode=productcode,location=location,paymentcode=paymentcode, message=message, remarks=remarks)
    return render(request, 'form.html')