# accounts/urls.py
from django.urls import path
from .views import signin_view, signup_view, signout_view

urlpatterns = [
    path('signin/', signin_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('signout/', signout_view, name='signout'),
]
