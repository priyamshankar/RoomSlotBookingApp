from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('booking',views.booking,name='booking'),
    path('customerList',views.customerList, name='customerList')
]
