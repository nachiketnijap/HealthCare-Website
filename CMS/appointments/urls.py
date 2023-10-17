from . import views 
from django.urls import path
from .views import update_appointment,appointment_list,delete_appointment
urlpatterns =[
    path('schedule_appointment/',views.schedule_appointment,name='schedule_appointment'),
    path('update/<int:pk>/', update_appointment, name='update_view'),
    path('appointment_list/', appointment_list, name='appointment_list'),
    path('delete/<int:pk>', delete_appointment, name='delete_appointment'),
    path('search_list/',views.todays_schedule,name='search_list'),
]