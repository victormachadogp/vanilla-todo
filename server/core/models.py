from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

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
    description = models.TextField(max_length=255)
    completed = models.BooleanField(null=True, blank=True)
    watch = models.BooleanField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)
    order = models.IntegerField(null=True)
    creation_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title        
    
    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"