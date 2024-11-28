from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import AlbumModel
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView


class Add_Album(CreateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')

class Edit_Album(UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    pk_url_kwarg = 'id'
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')


class Delete_Album(DeleteView):
    model = AlbumModel
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('homepage')
