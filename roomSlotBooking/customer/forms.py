from django.forms import ModelForm
from .models import *


class bookingForm(ModelForm):
    class Meta:
        model = booking
        fields = '__all__'  # or in a array ['room','Customers']


class roomForm(ModelForm):
    class Meta:
        model = room
        fields = '__all__'
