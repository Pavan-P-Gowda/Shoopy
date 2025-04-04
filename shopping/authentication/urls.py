from django.urls import path 

#  importing necessery views 
from .views import UserRegister, UserLogin 

urlpatterns = [
    path('login', UserLogin.as_view(), name = 'signin'),
    path('register',UserRegister.as_view(), name = 'signup')
]