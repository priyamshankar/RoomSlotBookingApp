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

    isBooked=models.BooleanField(default=true)
    Customers=models.ForeignKey(Customers,null=True,on_delete=models.SET_NULL)



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
    room=models.ForeignKey(room,null=True,on_delete=models.SET_NULL)
    Customers=models.ForeignKey(Customers,null=True,on_delete=models.SET_NULL)

    dateBooked=models.DateTimeField(auto_now_add=true,null=true)
    # timerslots=models.IntegerField()
    rules=models.ForeignKey(rules,null=True,on_delete=models.SET_NULL)
    DAYSLOT=(
        ('fullDay','fullday'),
        ('6am to 10am','6am to 10am'),
        ('10am to 3pm','10am to 3pm'),
        ('3pm to 10pm','3pm to 10pm'),
        ('10pm to 6am','10pm to 6am')
    )
    timeslots=models.CharField(max_length=200,choices=DAYSLOT)
    #time slots are temproary for now but later it will be fetched from the table

class records(models.Model):
    booking=models.ForeignKey(booking,null=true,on_delete=models.SET_NULL)
    room=models.ForeignKey(room,null=True,on_delete=models.SET_NULL)
    Customers=models.ForeignKey(Customers,null=True,on_delete=models.SET_NULL)
    # timerslots=models.IntegerField()
    # cName=models.CharField(max_length=200,null=true)
    # userId=models.CharField(max_length=200,null=true)
    # email=models.EmailField(null=true)