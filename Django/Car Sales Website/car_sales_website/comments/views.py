from .models import Comment
from .forms import CommentForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class AddComment(CreateView):
    form_class= CommentForm
    model = Comment
    template_name = 'add_comment.html'
    success_url = reverse_lazy('car_listing')