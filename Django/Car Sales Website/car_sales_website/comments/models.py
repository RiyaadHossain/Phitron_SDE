from cars.models import Car
from django.db import models

class Comment(models.Model):
    commented_by = models.CharField(max_length=50)
    comment = models.CharField(max_length=255)
    commented_at = models.DateField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment