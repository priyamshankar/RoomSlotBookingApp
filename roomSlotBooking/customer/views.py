from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    rooms = room.objects.all()
    rule = rules.objects.all()
    # totalroom=rules.objects.get(totalRooms)
    for j in rule:
        totalroom = j.totalRooms
    bookedRoomCount = 0
    for i in rooms:
        # print("hiii")
        if i.isBooked == 1:
            # bookedRoomCount = int(bookedRoomCount)+1
            bookedRoomCount+=1
    roomLeft = int(totalroom)-int(bookedRoomCount)
    params = {
        'roomLeft': roomLeft, 'totalroom': totalroom
    }
    return render(request, 'home.html', params)


def bookingCust(request, custId):

    bookings = booking.objects.all()
    customer = Customers.objects.get(id=custId)

    # booking_set is a dynamic thing, it changes as the model changes
    roomBook = customer.booking_set.all()
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
    rule = rules.objects.all()
    params = {
        'rule': rule
    }

    return render(request, 'rules.html', params)
