from django.db import models

# Create your models here.
class OrderModel(models.Model):

    fullname = models.CharField(max_length=250, blank=True, null=True)
    email =  models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250,blank=True, null=True)
    productname = models.CharField(max_length=250, blank=True, null=True)
    productcode = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    paymentcode = models.CharField(max_length=250, blank=True, null=True)
    message = models.CharField(max_length=250, blank=True, null=True)
    

    def __str__(self):
        return str(self.fullname)

