from django.db import models
from django.forms import IntegerField
from sqlalchemy import false, true

# Create your models here.

class Customers(models.Model):
    name=models.CharField(max_length=200,null=true)
    userId=models.CharField(max_length=200,null=true)
    password=models.CharField(max_length=50,null=true)
    email=models.EmailField(null=true)

    def __str__(self):
        return self.name


class manager(models.Model):
    name=models.CharField(max_length=200,null=true)
    userId=models.CharField(max_length=200,null=true)
    password=models.CharField(max_length=50,null=true)
    email=models.EmailField(null=true)
    def __str__(self):
        return self.name

class room(models.Model):

    isBooked=models.BooleanField(default=false)

class rules(models.Model):
    EARLYBOOK = (
        ('oneday','oneday'),
        ('twoday','twoday'),
        ('threeday','threeday'),
        ('fourDay','fourday'),
        ('fiveDay','fiveday'),
    )
    DAYSLOT=(
        ('fullDay','fullday'),
        ('6am to 10am','6am to 10am'),
        ('10am to 3pm','10am to 3pm'),
        ('3pm to 10pm','3pm to 10pm'),
        ('10pm to 6am','10pm to 6am')
    )
    totalRooms=models.IntegerField()
    timeslots=models.CharField(max_length=200,choices=DAYSLOT)
    advanceBooking=models.CharField(max_length=200,choices=EARLYBOOK)

class booking(models.Model):
    dateBooked=models.DateTimeField(auto_now_add=true,null=true)
    timerslots=models.IntegerField()

class records(models.Model):
    dateBooked=models.DateTimeField(auto_now_add=true,null=true)
    timerslots=models.IntegerField()
    cName=models.CharField(max_length=200,null=true)
    userId=models.CharField(max_length=200,null=true)
    email=models.EmailField(null=true)