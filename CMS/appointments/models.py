from django.db import models
from doctors.models import Doctor
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError
# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def Date_validation(value):
            if value < datetime.date.today():
                raise ValidationError("The date cannot be in the past")
    date = models.DateField(default=datetime.date.today, validators=[Date_validation])
    time = models.TimeField()
    entered_by =models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    
