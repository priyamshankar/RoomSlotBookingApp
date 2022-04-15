from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render (request,'home.html')

def booking(request):
    return render (request, 'booking.html')

def customerList(request):
    return render(request,'customer.html')
