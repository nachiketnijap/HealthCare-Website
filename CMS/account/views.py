from django.shortcuts import render,redirect
# from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm
from django.contrib import messages
# from appointments.views import appointment_list
# from products.views import ProductListView
from django.contrib.auth import logout

def register(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request,'base/register.html',{'form_data':form})
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request,'Account Created Successfully for '+user_name)
            return redirect('/super/emplist')
        
        else:
            messages.error(request,'OOPS Some Issue in Your Form')
            return render(request,'base/register.html',{'form_data':form})
        
    return render(request,'base/register.html',{'form_data':form})


class MyLoginView(LoginView):
    def form_valid(self, form):
        # messages.success(self.request,"Logged in successfully ")
        return super().form_valid(form)
    def form_invalid(self, form):
        # messages.error(self.request," invalid username or password  ")
        return super().form_invalid(form)
    
def MyLogoutView(request):
    logout(request)
    return redirect('/') 