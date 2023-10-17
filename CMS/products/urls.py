from django.urls import path
from .views import ProductListView,ProductCreateView,ProductUpdateView, ProductDeleteView
from .import views
app_name = 'products'

# Create your views here.
urlpatterns = [
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('', ProductListView.as_view(), name='list1'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),

]