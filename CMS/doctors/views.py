from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView, DeleteView
from .models import Doctor
from .forms import DoctorForm 
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required




@method_decorator(login_required(login_url='/'), name='dispatch')
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/doctorlist.html'
    context_object_name = 'doctors'

@method_decorator(login_required(login_url='/'), name='dispatch')
class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctorform.html'
    success_url = reverse_lazy('doctors:doctorlist')

    def form_valid(self, form):
        messages.success(self.request,('Doctor Data Added Successfully !'))
        return super().form_valid(form)
    
    
@method_decorator(login_required(login_url='/'), name='dispatch')
class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctorform.html'
    success_url = reverse_lazy('doctors:doctorlist')

    def form_valid(self, form):
        messages.success(self.request,('Doctor Data Updated Successfully !'))
        return super().form_valid(form)
    
    

@method_decorator(login_required(login_url='/'), name='dispatch')
class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctors/doctorconfirm_delete.html'
    success_url = reverse_lazy('doctors:doctorlist')

    def form_valid(self, form):
        messages.success(self.request,('Doctor Data Deleted Successfully !'))
        return super().form_valid(form)
    
    



