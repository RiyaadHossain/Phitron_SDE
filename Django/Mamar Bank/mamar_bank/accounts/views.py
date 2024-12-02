from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm,UserPasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views import View
from django.shortcuts import redirect
from transactions.views import send_email_to

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

def log_out(req):
    logout(req)
    return redirect('home')


class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        password_change_form = UserPasswordChangeForm(user=request.user)
        return render(request, self.template_name, {'form': form, 'password_change_form': password_change_form})

    def post(self, request):
        if 'password_change_form' in request.POST:
            password_change_form = UserPasswordChangeForm(user = request.user, data=request.POST)
            if password_change_form.is_valid():
                password_change_form.save()
                update_session_auth_hash(request, request.user)

                subject = "Password Changed"
                message = "Alert! Someone changed your password on Mamar Bank"
                send_email_to(self, subject, message, [request.user.email])

                return redirect('profile')
            form = UserUpdateForm(instance=request.user)
        elif 'form' in request.POST:
            form = UserUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile') 
            password_change_form = UserPasswordChangeForm(user=request.user)
        else: 
            form = UserUpdateForm(instance=request.user)
            password_change_form = UserPasswordChangeForm(user=request.user)

        return render(request, self.template_name, {'form': form, 'password_change_form': password_change_form})
    
    
    