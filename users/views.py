from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def home(request):
    return render(request, 'home.html')

def register(request):
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    
    return render(request, 'users/register.html', {'form':form})

def login(request):
    if request.user.is_authenticated:
        return redirect('/home/')
        
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('task-list')
    else:
        form = LoginForm()
    
    return render(request, 'users/login.html', {'form':form})

def logout(request):
    auth_logout(request)
    return redirect('/accounts/login/')



