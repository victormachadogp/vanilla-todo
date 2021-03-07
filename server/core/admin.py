from django.contrib import admin
from .models import Tasklist, Task

# Register your models here.

admin.site.register(Tasklist)
admin.site.register(Task)
