from django import forms
from .models import Appointment
from django.contrib.auth.models import User
from doctors.models import Doctor


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Doctor'}))
    def label_from_instance(self, obj):
        return obj.name
    date = forms.DateField(required=True,widget = forms.DateInput(attrs={'class':'form-control','placeholder':'select date '}))
    time = forms.TimeField(required=True,widget = forms.TimeInput(attrs={'class':'form-control','placeholder':'select  time '}))
    entered_by = forms.ModelChoiceField(queryset=User.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Employee'}))

    
