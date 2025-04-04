from django.shortcuts import render
from django.views.generic import CreateView

from django.urls import reverse_lazy


# importing the inbuilt user regesteration from calss :> usercretaionform
from django.contrib.auth.forms import UserCreationForm

# importing the inbuilt user loginview to inherritens and override the from and template
from django.contrib.auth.views import LoginView

# Create your views here.
class UserRegister(CreateView):
    from_class = UserCreationForm 
    template_name = 'signup.html'
    # find the sig-in page path on succeessfull registaion and sendd the useer there
    success_url = reverse_lazy('singin')

class UserLogin(LoginView):
    template_name = 'signin.html'
