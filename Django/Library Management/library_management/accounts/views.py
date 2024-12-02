from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm, DepositForm
from .models import Profile

def send_email_to_user(subject, message, recipient_list):
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

def register(req):
    form = RegisterForm()
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login_page')
        
    return render(req, 'register.html', {'form':form})

def log_in(req):
    form = AuthenticationForm()
    if req.method == 'POST':
        form = AuthenticationForm(req,data=req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(req, user)
                return redirect('homepage') 
        
    return render(req, 'login.html', {'form':form})

def log_out(req):
    logout(req)
    return redirect('login_page')

def deposit(req):
    form = DepositForm()
    if req.method == 'POST':
        form = DepositForm(data=req.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            profile = Profile.objects.get(user=req.user)
            profile.balance += amount
            profile.save()

            subject = "Deposit Money"
            message = f"Deposite {amount} successfully"
            recipient_list = [req.user.email]

            send_email_to_user(subject, message, recipient_list)

            return redirect('homepage') 
        
    return render(req, 'deposit.html', {'form':form})