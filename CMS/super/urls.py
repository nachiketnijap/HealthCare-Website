from django.urls import path
from  .import views
from .views import EmployeeListView,EmployeeDeleteView,EmployeeUpdateView
# app_name = 'super'

urlpatterns = [
    path('emplist/', EmployeeListView.as_view(), name='emplist'),
    path('employeeupdate/<int:pk>/', EmployeeUpdateView.as_view(), name='employeeupdate'),
    path('employeedelete/<int:pk>/', EmployeeDeleteView.as_view(), name='employeedelete'),
    path('doctor-visits/', views.doctor_visits_view, name='doctor_visits'),
    path('deals-done/', views.deals_done_view, name='deals_done'),
    path('product-list/', views.product_list_view, name='product_list'),

]
