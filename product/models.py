from django.db import models

# Create your models here.
class ProductModel(models.Model):

    productname = models.CharField(max_length=250, blank=True, null=True)
    productcode = models.CharField(max_length=250, blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return str(self.productname)

