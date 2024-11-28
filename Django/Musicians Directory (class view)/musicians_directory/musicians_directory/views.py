from django.shortcuts import render
from album.models import AlbumModel

def home(req):
    albums = AlbumModel.objects.all()
    return render(req, 'home.html', {'albums':albums})