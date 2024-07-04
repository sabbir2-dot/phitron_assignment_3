from django.db import models
from category.models import Category
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
