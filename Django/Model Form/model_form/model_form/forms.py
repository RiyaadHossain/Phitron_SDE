from django.forms import forms, ModelForm
from form_app.models import StudentModel

class StudentForm(ModelForm):
    class Meta:
        model = StudentModel
        exclude = ['roll']
        labels = {
            'name': 'Enter your name'
        }

        help_texts = {
            'age': 'Must be <= 50'
        }

