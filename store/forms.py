from django.forms import ModelForm
from .models import Customer, Product, Category, Order
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }