from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from .models import Tasklist
# Create your views here.

# Query do banco, pegar os objetos e gravar em variavel
# Para cada objeto, criar uma lista de objetos Json.(Serialization)

def get_tasklists(request):
    tasks = Tasklist.objects.all().values()  # or simply .values() to get all fields
    task_list = list(tasks)  # important: convert the QuerySet to a list object

    return JsonResponse(task_list, safe=False)



