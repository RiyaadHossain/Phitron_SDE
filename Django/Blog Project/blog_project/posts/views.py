from django.shortcuts import render,redirect
from . import forms
from .models import PostModel

def add_post(req):
    if req.method == 'POST':
        form = forms.PostForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.PostForm()

    return render(req, 'add_post.html', {'form':form})

def edit_post(req,id):
    post_instance = PostModel.objects.get(pk=id)
    if req.method == 'POST':
        form = forms.PostForm(req.POST, instance=post_instance)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.PostForm(instance=post_instance)

    return render(req, 'edit_post.html', {'form':form})

def delete_post(req, id):
    post = PostModel.objects.get(pk=id)
    post.delete()
    return redirect('homepage')