from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
def positive_validator(value):
    if value <= 0:
        raise ValidationError('Value must be a positive integer greater than zero.')

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product_images',default=None)
    product_price = models.PositiveIntegerField(validators=[positive_validator])
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.product_name

