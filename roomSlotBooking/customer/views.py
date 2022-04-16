from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    return render(request, 'home.html')


def bookingCust(request, custId):

    bookings = booking.objects.all()
    customer = Customers.objects.get(id=custId)

    roomBook = customer.booking_set.all() #booking_set is a dynamic thing, it changes as the model changes
    # print(customer)
    params = {
        # 'booking': bookings, 'roomBook': int(custId)
        'booking': bookings, 'roomBook': roomBook
    }
    return render(request, 'bookingCust.html', params)

def bookingCl(request):
    bookings = booking.objects.all()

    params = {
        'booking': bookings
    }
    return render(request, 'booking.html', params)
    

def customerList(request):
    return render(request, 'customer.html')


def context(request):
    rule=rules.objects.all()
    params={
        'rule':rule
    }

    return render (request,'rules.html', params)