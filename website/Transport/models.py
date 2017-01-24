from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.

class Booking(models.Model):
	startpoint = models.CharField(max_length=250)
	destination = models.CharField(max_length=200)
	date=models.DateTimeField('date of booking')
		
