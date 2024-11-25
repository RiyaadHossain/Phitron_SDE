from django.db import models
from authors.models import AuthorModel

class ProfileModel(models.Model):
    name = models.CharField(max_length=15)
    about = models.TextField(max_length=200)
    author = models.OneToOneField(AuthorModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


