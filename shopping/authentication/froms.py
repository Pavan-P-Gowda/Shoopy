#  this files is to building custom forms.

#  importing the inbuilt forms 
from django import forms

# importing authenticcationforms django's inbulit authentication 
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    