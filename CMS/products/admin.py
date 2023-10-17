from django.contrib import admin
from .models import Product
from django.utils.html import format_html

# Register your models here.
class customAdmin(admin.ModelAdmin):
    list_display=['product_name','company_name','product_price','products_image']
    def products_image(self,obj):
        return format_html('<img src="{}" width="90" height="100" />',obj.product_image.url)


admin.site.register(Product,customAdmin)