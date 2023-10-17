from django.urls import path
from .views import DoctorListView,DoctorCreateView,DoctorUpdateView, DoctorDeleteView
app_name = 'doctors'

# Create your views here.
urlpatterns = [
    path('doctorlist/', DoctorListView.as_view(), name='doctorlist'),
    path('doctorcreate/', DoctorCreateView.as_view(), name='doctorcreate'),
    path('doctorupdate/<int:pk>/', DoctorUpdateView.as_view(), name='doctorupdate'),
    path('doctordelete/<int:pk>/', DoctorDeleteView.as_view(), name='doctordelete'),
]