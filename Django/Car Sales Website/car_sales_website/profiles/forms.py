from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            del self.fields['password'] 