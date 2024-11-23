from django.db import models
from django.core import validators

# Create your models here.
class StudentModel(models.Model):    
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
    }
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    age = models.IntegerField(validators=[validators.MinValueValidator(15, "Must be greater than 15"), validators.MaxValueValidator(25)])
    address = models.TextField()
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


    def __str__(self):
        return f"{self.name} - {self.roll}"