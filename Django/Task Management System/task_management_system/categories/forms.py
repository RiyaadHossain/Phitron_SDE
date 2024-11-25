from django.forms import ModelForm
from .models import TaskCategoryModel

class CategoryForm(ModelForm):
    
    class Meta:
        model = TaskCategoryModel
        fields = "__all__"
