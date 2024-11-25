from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import MusicianModel

# Create your views here.
def add_musician(req):
    if req.method == 'POST':
        form = MusicianForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        return render(req, 'add_musician.html', {'form': form})
    
    form = MusicianForm()
    return render(req, 'add_musician.html', {'form': form})

def edit_musician(req, id):
    musician = MusicianModel.objects.get(pk=id)
    if req.method == 'POST':
        form = MusicianForm(req.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        return render(req, 'edit_musician.html', {'form': form})
    
    form = MusicianForm(instance=musician)
    return render(req, 'edit_musician.html', {'form': form})