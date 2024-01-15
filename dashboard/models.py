from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class notes(models.Model):
    user = models.ForeignKey(User , on_delete =models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length= 500)
    
    def __str__(self):
        return self.title
    

class Homework(models.Model):
    user = models.ForeignKey(User , on_delete =models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # due = models.DateTimeField(auto_now=True)
    due = models.DateField()
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return self.subject
    
class Todo(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title