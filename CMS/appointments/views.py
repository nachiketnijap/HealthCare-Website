
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from doctors.models import Doctor
from .models import Appointment
from .forms import AppointmentForm
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required




@login_required(login_url='/')

def schedule_appointment(request):
    doctors = Doctor.objects.all()
    users= User.objects.all()
    
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        entered_by_id = request.POST.get('entered_by')
        
        doctor = Doctor.objects.get(id=doctor_id)
        entered_by=User.objects.get(id=entered_by_id)
        appointment = Appointment(
            doctor=doctor,
            date=date,
            time=time,
            entered_by=entered_by
        )
        appointment.save()
        messages.success(request, 'Appointment Scheduled Successfully !')
        return redirect('appointment_list')
    context = {'doctors': doctors, 'users':users}
    return render(request, 'appointments/schedule.html', context)                           


@login_required(login_url='/')
def update_appointment(request, pk):
    obj = Appointment.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment Updated Successfully !')
            return redirect('appointment_list')
            
    else:
        form = AppointmentForm(instance=obj)
    
    context = {'form': form,}
    return render(request, 'appointments/form.html', context)


@login_required(login_url='/')
def appointment_list(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'appointments/list.html', context)


@login_required(login_url='/')
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment Deleted Successfully !')
        return redirect('appointment_list')
        
    
    context = {'appointment': appointment}
    return render(request, 'appointments/delete_appointment.html', context)


@login_required(login_url='/')
def todays_schedule(request):
    today = datetime.now().date()
    result = Appointment.objects.filter(date=today)
    context={
            'object':result
        }
    return render(request,'appointments/search-list.html',context)
