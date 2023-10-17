from django import forms
from .models import Doctor
from django.contrib.auth.models import User



class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
    name = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Doctor Name'}))
    specialisation = forms.ChoiceField(
        choices=[('Chest', 'Chest'),
                 ('Heart', 'Heart'),
                 ('General', 'General'),('Orthopaedic', 'Orthopaedic')],
                 required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Specialisation'}))
    contact_number = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter  Number'}))
    location = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Location'}))
    entered_by = forms.ModelChoiceField( queryset=User.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Employee'}))