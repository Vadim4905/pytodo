from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    iscomplete = models.BooleanField(default=False)
    ismissed = models.BooleanField(default=False)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Subtask(models.Model):
    name =models.CharField(max_length=100)
    iscomplete = models.BooleanField(default=False)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)

