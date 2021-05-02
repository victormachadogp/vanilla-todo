"""server URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core import serializers
from .models import Tasklist
import sys, json


@csrf_exempt
@require_http_methods(["GET","POST"]) 
def tasklists(request):    
    if request.method == "GET":
        try:
            tasks = Tasklist.objects.all().values()  
        except Tasklist.DoesNotExist: 
            return JsonResponse(
                {'message': 'Tasklists do not exist'}, 
                status = 404
            ) 

        task_list = list(tasks)  
        return JsonResponse(task_list, safe=False)

    else:
        data = json.loads(request.body)

        tsk = Tasklist()
        if "title" in data: 
            tsk.title = data['title']
        if "color" in data:  
            tsk.color = data['color']
        if "order" in data:
            tsk.order = data['order']  

        if not tsk.title:
            return JsonResponse(
                {'message': 'Required Title field'},
                status=422
            )

        try:
            tsk.save()
        except:
            return JsonResponse(
                {'message': sys.exc_info()[0]},
                 status=500)
       
        return JsonResponse(
            {'message': 'Created'},
            status=201
        )


@require_http_methods(["PUT","DELETE","GET"])
def tasklistsid(request, tasklist_id):
    try: 
        tasklist = Tasklist.objects.get(id=tasklist_id)         
    except Tasklist.DoesNotExist: 
        return JsonResponse({'message': 'Tasklist_id does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == "GET":
        return JsonResponse(model_to_dict(tasklist), safe=False)
    elif request.method == "PUT": 
        return HttpResponse("PUT")     
    else: 
        return HttpResponse("DELETE") 

# Tasklists
# GET /tasklists/ - retorna todas as tasklists -  ✅
# GET /tasklists/:id/ - retorna apenas uma tasklist ✅ 
# POST /tasklists/ - cria uma nova tasklist ✅
# PUT/PATCH? /tasklists/:id/ - atualiza apenas uma tasklist
# DELETE /tasklists/:id/ - deleta apenas uma tasklist

# Tasks
# GET /tasklists/:id/tasks/ - retorna todas as tasks de uma determinada tasklist
# POST /tasklists/:id/tasks/ - cria uma nova task
# PUT/PATCH? /tasks/:id/ - atualiza apenas uma task de uma determinada tasklist
# DELETE /tasks/:id/ - deleta apenas uma task



