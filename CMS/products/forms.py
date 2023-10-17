from django import forms
from .models import Product
from django.contrib.auth.models import User



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
    product_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Product Name'})
    )

    company_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter company name'}))

    product_image = forms.ImageField()

    product_price = forms.DecimalField(required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter price ','min':'0'}))

    entered_by = forms.ModelChoiceField(queryset=User.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Employee'}))