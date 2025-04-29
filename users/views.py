from django.shortcuts import render,redirect
from .forms import *

def home(request):
    return render(request, 'layout.html')

def register(request):
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'users/register.html', {'form':form})

def login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'users/login.html', {'form':form})



