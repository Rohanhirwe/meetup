from django import forms
from .models import user
from django.contrib.auth.models import AbstractUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = user
        fields = ('username','password','email','address')