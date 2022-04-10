from django.db import models
from django import forms
# Create your models here.

class regform(models.Model):
    name = models.CharField(max_length=100 )
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    uniqueid=models.CharField(max_length=20)

class detailform(models.Model):
    age=models.CharField(max_length=3)
    height=models.IntegerField()
    weight=models.IntegerField()
    sex = models.CharField(max_length=10)
    blood=models.CharField(max_length=3)
    pin=models.IntegerField()
    uniqueid = models.CharField(max_length=20)
    

class medical(models.Model):
    dname=models.CharField(max_length=50)
    datetime=models.CharField(max_length=50)
    visit=models.CharField(max_length=250)
    medications=models.CharField(max_length=250)
    uniqueid = models.CharField(max_length=20)    
