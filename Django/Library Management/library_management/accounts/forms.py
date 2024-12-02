from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=30, required=True)
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(), label="Password")

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class DepositForm(forms.Form):
    amount = forms.IntegerField(max_value=500000, min_value=500)