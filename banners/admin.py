from django.contrib import admin
from banners.models import BannerModel
# Register your models here.
class Banners(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']

admin.site.register(BannerModel, Banners)