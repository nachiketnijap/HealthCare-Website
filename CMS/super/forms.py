from django import forms
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','is_active']
    
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'})
    )

    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'})
    )

    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'})
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'})
    )

    # date_joined = forms.DateField(
    #     required=True,
    #     widget = forms.DateInput(attrs={'type': 'date','class':'form-control','placeholder':'select date '}))

    is_active = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'})
    )




class DoctorVisitsForm(forms.Form):
    employee_name = forms.ModelChoiceField(queryset=User.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Employee'}))
    month = forms.ChoiceField(choices=[(1, 'January'), (2, 'February'), (3,'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')],required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Specialisation'}))  

class DealsDoneForm(forms.Form):
    employee_name = forms.ModelChoiceField(queryset=User.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Employee'}))
    month = forms.ChoiceField(choices=[(1, 'January'), (2, 'February'), (3,'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')],required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Specialisation'}))  


class ProductListForm(forms.Form):
    employee_name = forms.ModelChoiceField(queryset=User.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-select','placeholder':'Select Employee'}))

