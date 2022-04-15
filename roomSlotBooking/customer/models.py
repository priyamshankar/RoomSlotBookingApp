from django.db import models
from sqlalchemy import true

# Create your models here.

class Customers(models.Model):
    name=models.CharField(max_length=200,null=true)
    userId=models.CharField(max_length=200,null=true)
    password=models.CharField(max_length=50,null=true)

