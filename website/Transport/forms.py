from django import forms
from django.contrib.auth.models import User
from .models import Booking


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class BookingForm(forms.ModelForm):
    class Meta:
	model = Booking
	fields = ['startpoint','destination','date']
