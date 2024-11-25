from django.forms import ModelForm
from .models import CategoryModel


class CategoryForm(ModelForm):
    
    class Meta:
        model = CategoryModel
        fields = "__all__"
