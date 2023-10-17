from django import forms
from .models import Deal
from doctors.models import Doctor
from products.models import Product
from django.contrib.auth.models import User



class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = '__all__'
    doc_name = forms.ModelChoiceField(queryset=Doctor.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Employee'}))
    product_name = forms.ModelChoiceField(queryset=Product.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Employee'}))
    quantity_ordered = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter quantity ordered','min':'1'}))
    date=forms.DateField(required=True,widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Date'}))
    entered_by = forms.ModelChoiceField(queryset=User.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Employee'}))