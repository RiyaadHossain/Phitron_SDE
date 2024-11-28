from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

class OrderHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)