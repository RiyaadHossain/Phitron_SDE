from django.shortcuts import render
from . import forms

# Create your views here.
def add_profile(req):
    if req.method == 'POST':
        form = forms.ProfileForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'add_profile.html', {'form':form})
    else:
        form = forms.ProfileForm()
    return render(req, 'add_profile.html', {'form':form})