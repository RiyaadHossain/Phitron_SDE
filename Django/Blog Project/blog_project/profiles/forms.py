from django.forms import ModelForm
from profiles.models import ProfileModel


class ProfileForm(ModelForm):
    
    class Meta:
        model = ProfileModel
        fields = "__all__"
