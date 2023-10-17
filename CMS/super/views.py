from django.shortcuts import render,redirect
from django.db.models import Count
from appointments.models import Appointment
from products.models import Product
from django.urls import reverse_lazy
from deals.models import Deal
from .forms import DoctorVisitsForm,DealsDoneForm,EmployeeForm,ProductListForm
from django.views.generic import ListView,UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required(login_url='/'), name='dispatch')
class EmployeeListView(ListView):
    model = User
    template_name = 'super/employeelist.html'
    context_object_name = 'super'

@method_decorator(login_required(login_url='/'), name='dispatch')
class EmployeeUpdateView(UpdateView):
    model = User
    form_class = EmployeeForm
    template_name = 'super/employeeform.html'
    success_url = reverse_lazy('emplist')
    def form_valid(self, form):
        messages.success(self.request,('Successfully Updated Employee Data !'))
        return super().form_valid(form)

@method_decorator(login_required(login_url='/'), name='dispatch')
class EmployeeDeleteView(DeleteView):
    model = User
    template_name = 'super/employeeconfirm_delete.html'
    success_url = reverse_lazy('emplist')
    def form_valid(self, form):
        messages.success(self.request,('Successfully Deleted Employee Data !'))
        return super().form_valid(form)

@login_required(login_url='/')
def doctor_visits_view(request):
    if request.method == 'POST':
        form = DoctorVisitsForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee_name']
            month = form.cleaned_data['month']
            
            visits_data = Appointment.objects.filter(entered_by=employee, date__month=month).values('entered_by').annotate(total_appointments=Count('id'))
            
            return render(request, 'super/doctor_visits.html', {'visits_data': visits_data, 'emp':employee.username})

    else:
        form = DoctorVisitsForm()

    return render(request, 'super/doctor_visits_form.html', {'form': form})


@login_required(login_url='/')
def deals_done_view(request):
    if request.method == 'POST':
        form = DealsDoneForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee_name']
            month = form.cleaned_data['month']
            
            deals_data = Deal.objects.filter(entered_by=employee, date__month=month).values('entered_by').annotate(total_deals=Count('id'))
            
            return render(request, 'super/deals_done.html', {'deals_data': deals_data, 'emp':employee.username})

    else:
        form = DealsDoneForm()

    return render(request, 'super/deals_done_form.html', {'form': form})

@login_required(login_url='/')
def product_list_view(request):
    if request.method == 'POST':
        form = ProductListForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee_name']
            
            
            products_data = Product.objects.filter(entered_by=employee)
            
            return render(request, 'super/product_list.html', {'products_data': products_data, 'emp':employee.username})

    else:
        form = ProductListForm()

    return render(request, 'super/product_list_form.html', {'form': form})
