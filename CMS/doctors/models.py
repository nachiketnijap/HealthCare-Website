from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here

class Doctor(models.Model):
    SPECIALISATION_CHOICES = (
        ('Chest', 'Chest'),
        ('Heart', 'Heart'),
        ('General', 'General'),
        ('Orthopaedic', 'Orthopaedic'),
        
    )

    name = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=50, choices=SPECIALISATION_CHOICES)
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{10}$',
        message='Phone number must be entered in the format: "9999999999". Exactly 10 digits allowed.',
        code='invalid_phone_number'
    )
    contact_number = models.CharField(
        validators=[phone_regex],
        max_length=10,
    )
    location = models.CharField(max_length=100)
    entered_by =models.ForeignKey(User,on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


