from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView, DeleteView
from .models import Product
from .forms import ProductForm 
from doctors.models import Doctor
from products.models import Product
from appointments.models import Appointment
from django.contrib.auth.models import User
from django.contrib import messages
from deals.models import Deal
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# from django.db.models import Sum
# >>> from deals.models import Deal
# >>> result=Deal.objects.values('doc_name').annotate(quantity_ordered=Sum('quantity_ordered'))

# print(result)
# <QuerySet [{'doc_name': 5, 'quantity_ordered': 56}, {'doc_name': 9, 'quantity_ordered': 78}, {'doc_name': 17, 'quantity_ordered': 37},
#  {'doc_name': 18, 'quantity_ordered': 10}]


# Create your views here
@login_required(login_url='/') 
def dashboard_view(request):
    results=Deal.objects.values('doc_name').annotate(quantity_ordered=Sum('quantity_ordered'))
    deals=Deal.objects.all()
    dc = Doctor.objects.all().count()
    pc = Product.objects.all().count()
    ac = Appointment.objects.all().count()
    us = User.objects.all().count()

    d = {'dc': dc, 'pc': pc, 'ac': ac, 'us': us, 'deals':deals, 'results':results}
    return render(request,'base/index.html', d)
    
@method_decorator(login_required(login_url='/'), name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'

@method_decorator(login_required(login_url='/'), name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/form.html'
    success_url = reverse_lazy('products:list1')

    def form_valid(self, form):
        messages.success(self.request,('Successfully added a new product !'))
        return super().form_valid(form)
    
    
@method_decorator(login_required(login_url='/'), name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/form.html'
    success_url = reverse_lazy('products:list1')
    def form_valid(self, form):
        messages.success(self.request,('Product Data Updated Successfully !'))
        return super().form_valid(form)
    
    

@method_decorator(login_required(login_url='/'), name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/confirm_delete.html'
    success_url = reverse_lazy('products:list1')

    def form_valid(self, form):
        messages.success(self.request,('Product Data Deleted Successfully !'))
        return super().form_valid(form)
  





