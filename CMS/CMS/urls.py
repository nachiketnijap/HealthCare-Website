"""
URL configuration for CMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from account.views import MyLoginView,register
from account.views import MyLogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('doctors/', include('doctors.urls')),
    path('appointments/', include('appointments.urls')),
    path('deals/',include('deals.urls')),
    path('',MyLoginView.as_view(template_name='base/login.html'),name='login'),
    path('register/',register,name='register-page'),
    path('logout/',MyLogoutView,name='logout'),
    path('super/',include('super.urls')),

]

if settings:
    urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
