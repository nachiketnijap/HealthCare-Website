from django.contrib import admin
from .models import Appointment

# Register your models here.
class customAdmin(admin.ModelAdmin):
    list_display=['doctor','date','time']
    


admin.site.register(Appointment,customAdmin)