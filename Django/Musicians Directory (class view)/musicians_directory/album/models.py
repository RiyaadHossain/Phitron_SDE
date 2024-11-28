from django.core import validators
from django.db import models
from musicians.models import MusicianModel

class AlbumModel(models.Model):
    album_name = models.CharField(max_length=50)
    release_date = models.DateField()
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])

    def __str__(self):
        return self.album_name