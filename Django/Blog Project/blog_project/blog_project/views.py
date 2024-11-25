from django.shortcuts import render
from posts.models import PostModel

def home(req):
    posts = PostModel.objects.all()
    return render(req, 'home.html', {'posts': posts})