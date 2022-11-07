from django.urls import path
from home.views import homepage, aboutpage, shop_page, order_form

app_name = "home"

urlpatterns = [
    path('index/', homepage, name='homepage'),
    path('about/', aboutpage, name='aboutpage'),
    path('shop/', shop_page, name='shop_page'),
     path('form/', order_form, name='order_form'),
]