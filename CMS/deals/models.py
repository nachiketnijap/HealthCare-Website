from django.db import models
from doctors.models import Doctor
from products.models import Product
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError


# Create your models here.
class Deal(models.Model):
    doc_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    product_name=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity_ordered=models.IntegerField(default=1)
    def Date_validation(value):
            if value < datetime.date.today():
                raise ValidationError("The date cannot be in the past")
    date = models.DateField(default=datetime.date.today, validators=[Date_validation])
    entered_by =models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    

class CountDeals(models.Model):
    entered_by =models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    quantity_ordered =models.IntegerField(default=1)