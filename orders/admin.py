from django.contrib import admin
from orders.models import OrderModel
# Register your models here.
class Orders(admin.ModelAdmin):
    list_display=['id','fullname', 'email', 'phone', 'productname','productcode', 'location','paymentcode', 'message']
admin.site.register(OrderModel,Orders)
