from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField( max_length=254)
    age = models.IntegerField()
    # img = models.ImageField(upload_to='/uploads')
    bio = models.TextField(max_length=500)
    birthday = models.DateField()
    appointment = models.DateTimeField()

    def __str__(self):
        return self.name

