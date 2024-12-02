from .models import BookReview
from django.forms import ModelForm
from borrowing.models import Borrowing
from django.core.exceptions import ValidationError
from django import forms

class BookReviewForm(ModelForm):
    class Meta:
        model = BookReview
        fields = ['review_text']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the user from the form's kwargs
        self.book = kwargs.pop('book', None)  
        super().__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        if self.user is None:
            raise ValidationError("User must be provided for validation.")
    
        # Check if the user has borrowed the book before allowing the review
        if not Borrowing.objects.filter(user=self.user, book=self.book).exists():
            raise ValidationError("You can only review a book that you have borrowed.")
        
        return cleaned_data