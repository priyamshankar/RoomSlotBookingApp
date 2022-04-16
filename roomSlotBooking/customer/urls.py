from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('booking/<str:custId>',views.bookingCust,name='bookingCusts'),
    path('booking/',views.bookingCl,name='booking'),
    path('customerlist/',views.customerList, name='customerList'),
    path('rules/', views.context ,name='rules'),
    path('book/',views.book, name='book'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register')
]
