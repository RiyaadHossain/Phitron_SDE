from .models import Comment
from django.forms.models import ModelForm

class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ["commented_by", "comment"]

        labels = {
            "commented_by": "Your Name",
            "comment": "Your Opinion",
        }
