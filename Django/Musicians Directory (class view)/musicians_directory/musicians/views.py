from django.shortcuts import render,redirect
from .forms import MusicianForm
from django.urls import reverse_lazy
from .models import MusicianModel
from django.views.generic import CreateView, UpdateView


class Add_Musician(CreateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')

class Edit_Musician(UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    pk_url_kwarg = 'id'
    template_name = 'edit_musician.html'
    success_url = reverse_lazy('homepage')
