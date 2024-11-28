from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', help_text='', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', help_text='Enter the same password as before, for verification.', required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
