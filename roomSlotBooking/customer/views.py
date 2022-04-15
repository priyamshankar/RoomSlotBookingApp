from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    return render(request, 'home.html')


def bookingCl(request):
    bookings = booking.objects.all()
    return render(request, 'booking.html', {'booking': bookings})


def customerList(request):
    return render(request, 'customer.html')
