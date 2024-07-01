# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def signin(request):
    return HttpResponse( render(request, 'accounts/signin.html' ))

def signin(request):
    if request.method == 'GET':
        return render(request, 'accounts/signin.html', {'form': AuthenticationForm()})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            return render(request, 'accounts/signin.html', {'form': AuthenticationForm(),
                                                            'error': 'Both username and password are required'})
        
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'accounts/signin.html', {'form': AuthenticationForm(),
                                                            'error': 'Invalid username or password'})
        else:
            login(request, user)
            return redirect('base') 
        
def signup(request):    
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('base')
            except IntegrityError:
                return render(request, 'accounts/signup.html', {'form': UserCreationForm(),
                                                                'error': 'Invalid username or password'}) 
        else:
            return render(request, 'accounts/signup.html', {'form': UserCreationForm(),
                                                            'error': 'Invalid password'})
    else:
        return render(request, 'accounts/signup.html', {'form': UserCreationForm()})
    
    
@login_required
def signout(request):
    logout(request)
    return redirect('base')