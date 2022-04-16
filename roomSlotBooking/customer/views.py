from cairo import FORMAT_A1
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *

# Create your views here.

@login_required(login_url='login')
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
            bookedRoomCount += 1
    roomLeft = int(totalroom)-int(bookedRoomCount)
    params = {
        'roomLeft': roomLeft, 'totalroom': totalroom
    }
    return render(request, 'home.html', params)

@login_required(login_url='login')
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 
def bookingCl(request):
    bookings = booking.objects.all()

    params = {
        'booking': bookings
    }
    return render(request, 'booking.html', params)

@login_required(login_url='login')
def customerList(request):
    return render(request, 'customer.html')

@login_required(login_url='login')
def context(request):
    rule = rules.objects.all()
    params = {
        'rule': rule
    }

    return render(request, 'rules.html', params)

@login_required(login_url='login')
def book(request):
    form = bookingForm()
    form2 = roomForm()
    if request.method == 'POST':
        form2 = roomForm(request.POST)
        form = bookingForm(request.POST)
        if form.is_valid and form2.is_valid():
            form.save()
            form2.save()
            return redirect('/')
    context = {'form': form, 'form2': form2}
    return render(request, 'book.html', context)

@unauthenticated_user
def loginpg(request):
    # if request.user == 'AnonymousUser':
    #     print(request.user)
    if request.method == 'POST':
        username = request.POST.get('userName')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,'login id or password not matched')
    
    return render(request, 'login.html')

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account is created')
            return redirect(login)
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
