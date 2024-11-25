from django.db import models
from django.utils import timezone
from categories.models import TaskCategoryModel

class TaskModel(models.Model):
    task_titile = models.CharField( max_length=50)
    task_description = models.TextField(max_length=200)
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(default=timezone.now)
    category = models.ManyToManyField(TaskCategoryModel, related_name='tasks')