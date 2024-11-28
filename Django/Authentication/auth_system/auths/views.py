from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm
from django.contrib.auth import login,authenticate,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, ChangePasswordForm,CustomUserChangeForm

def sign_up(req):
    if req.user.is_authenticated:
        return redirect('profile')

    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "User signed up Successfully!")
            return redirect('log_in') 
    else:
        form = SignupForm()
    return render(req, 'sign_up.html', {'form': form})

def log_in(req):
    if req.user.is_authenticated:
        return redirect('profile')
    
    if req.method == 'POST':
        form = AuthenticationForm(req,data=req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                messages.success(req, "User logged in Successfully!")
                login(req, user)
                return redirect('profile') 
    else:
        form = AuthenticationForm()
    return render(req, 'log_in.html', {'form': form})

@login_required
def profile(req):
    context = dict()

    if req.method == 'POST':
        form = CustomUserChangeForm(instance= req.user,data=req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "User data changed Successfully!")
            return redirect('profile') 
    else:
        form = CustomUserChangeForm(instance= req.user)

    context['user'] = req.user
    context['form'] = form
    return render(req, 'profile.html', context)

def log_out(req):
    logout(req)
    messages.success(req, "Logged out successfully!")
    return redirect('log_in')

@login_required
def change_pass(req):
    if req.method == 'POST':
        form = ChangePasswordForm(req.user,data=req.POST)
        if form.is_valid():
            update_session_auth_hash(req, form.user)
            messages.success(req, "User password changed Successfully!")
            return redirect('profile') 
    else:
        form = ChangePasswordForm(req.user)
    return render(req, 'change_pass.html', {'form': form})

@login_required
def change_pass_(req):
    if req.method == 'POST':
        form = PasswordResetForm( req.POST)
        if form.is_valid():
            update_session_auth_hash(req, form.user)
            messages.success(req, "User password changed Successfully!")
            return redirect('profile') 
    else:
        form = PasswordResetForm()
    return render(req, 'change_pass.html', {'form': form})