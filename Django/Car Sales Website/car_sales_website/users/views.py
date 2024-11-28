from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from .forms import SignupForm

def sign_up(req):
    form = SignupForm()
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')

    return render(req, 'signup.html', {'form': form})


def log_in(req):
    if req.user.is_authenticated:
        return redirect('profile_page')
    
    form = AuthenticationForm()
    if req.method == 'POST':
        form = AuthenticationForm(req,data=req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(req, user)
                return redirect('profile_page') 
    
    return render(req, 'login.html', {'form': form})


def log_out(req):
    logout(req)
    return redirect('login_page')