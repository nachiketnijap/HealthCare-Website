from . import views 
from django.urls import path
from .views import update_deal,deal_list,delete_deal
urlpatterns =[
    path('product_deals/',views.doctor_deal,name='product_deals'),
    path('update/<int:pk>/', update_deal, name='update_deal'),
    path('deal_list/', deal_list, name='deal_list'),
    path('delete/<int:pk>', delete_deal, name='delete_deal'),
    # path('product_deals/',views.user_deal,name='product_deals'),
]