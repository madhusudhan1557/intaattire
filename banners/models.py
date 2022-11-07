from django.db import models

# Create your models here.
class BannerModel(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return str(self.title)