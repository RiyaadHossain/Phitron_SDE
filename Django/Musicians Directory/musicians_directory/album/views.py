from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import AlbumModel

# Create your views here.
def add_album(req):
    if req.method == 'POST':
        form = AlbumForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        return render(req, 'add_album.html', {'form': form})
    
    form = AlbumForm()
    return render(req, 'add_album.html', {'form': form})

def edit_album(req, id):
    album = AlbumModel.objects.get(pk=id)
    if req.method == 'POST':
        form = AlbumForm(req.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        return render(req, 'add_album.html', {'form': form})
    
    form = AlbumForm(instance=album)
    return render(req, 'add_album.html', {'form': form})

def delete_album(req, id):
    album = AlbumModel.objects.get(pk=id)
    album.delete()
    return redirect('homepage')