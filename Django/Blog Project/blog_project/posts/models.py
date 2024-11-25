from django.db import models
from categories.models import CategoryModel
from authors.models import AuthorModel

class PostModel(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField(max_length=200)
    category = models.ManyToManyField(CategoryModel)
    author = models.ForeignKey(AuthorModel, models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title


