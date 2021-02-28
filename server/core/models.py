from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.


class Tasklist(models.Model):
    id = models.IntegerField(primary_key=True)
#    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=20)
    color = models.CharField(max_length=6)
    order = models.IntegerField()

    def __str__(self):
        return self.title

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    tasklist = models.ForeignKey(Tasklist, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField()
    active = models.BooleanField()
