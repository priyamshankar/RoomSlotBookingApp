from attr import fields
from django.forms import ModelForm
from flask_login import user_accessed
from importlib_metadata import files
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class bookingForm(ModelForm):
    class Meta:
        model = booking
        fields = '__all__'  # or in a array ['room','Customers']


class roomForm(ModelForm):
    class Meta:
        model = room
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']