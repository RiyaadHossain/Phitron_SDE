from django.db import models
from brands.models import Brand

class Car(models.Model):
    car_name = models.CharField( max_length=50)
    description = models.TextField(max_length=250)
    image = models.ImageField( upload_to='media/')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField(default=2000)