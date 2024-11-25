from django.db import models

class AuthorModel(models.Model):
    name = models.CharField(max_length=15)
    bio = models.TextField(max_length=200)
    phone_no = models.IntegerField()

    def __str__(self):
        return self.name


