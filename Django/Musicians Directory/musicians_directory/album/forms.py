from django import forms
from django.forms import ModelForm
from .models import AlbumModel


class AlbumForm(ModelForm):
    
    class Meta:
        model = AlbumModel
        fields = "__all__"
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
        