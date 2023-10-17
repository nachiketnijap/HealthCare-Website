from django.contrib import admin
from .models import Doctor
# from django.utils.html import format_html

# Register your models here.
class customAdmin(admin.ModelAdmin):
    list_display=['name','specialisation','contact_number','location']



admin.site.register(Doctor,customAdmin)