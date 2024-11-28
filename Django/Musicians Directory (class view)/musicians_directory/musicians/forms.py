from django import forms
from django.forms import ModelForm
from .models import MusicianModel


class MusicianForm(ModelForm):
    # instrument_type = forms.MultipleChoiceField(choices=MusicianModel.INSTRUMENT_CHOICES, widget=forms.CheckboxSelectMultiple(), required=True)

    class Meta:
        model = MusicianModel
        fields = "__all__"
