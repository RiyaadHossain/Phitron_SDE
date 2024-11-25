from django import forms
from django.forms import ModelForm
from .models import TaskModel


class TaskForm(ModelForm):
    
    class Meta:
        model = TaskModel
        fields = "__all__"

        widgets = {
            'task_assign_date': forms.DateInput(attrs={'type':'date'}),
            'category': forms.CheckboxSelectMultiple()
        }
