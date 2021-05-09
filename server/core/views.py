from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core import serializers
from .models import Task, Tasklist
from django.db.utils import IntegrityError
import sys, json, logging


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


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def tasklistsid(request, tasklist_id):
    try: 
        tasklist = Tasklist.objects.get(id=tasklist_id)     
    except Tasklist.DoesNotExist: 
        return JsonResponse({'message': 'Tasklist_id does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == "GET":
        return JsonResponse(model_to_dict(tasklist), safe=False)
    elif request.method in ("PUT", "PATCH"):
        
        data = json.loads(request.body)
 
        try:
            Tasklist.objects.filter(id=tasklist_id).update(**data) 
        except IntegrityError: 
            return HttpResponse('ERRO - Id é invalido', status=404) 
       
        return HttpResponse('OK', status=200) 
         
    elif request.method == "DELETE":
        tasklist.delete()
        return JsonResponse({'message': 'Tasklist deleted with success!'}, status=204) 

#TASKS
@csrf_exempt
@require_http_methods(["GET","POST"]) 
def tasklists_id_tasks(request, tasklist_id):
    if request.method == "GET":
        tasks = Task.objects.filter(tasklist=tasklist_id).values()
        return JsonResponse(list(tasks), safe=False)
    else:
        data = json.loads(request.body)
        
        try: 
            tasklist = Tasklist.objects.get(id=tasklist_id)    
        except Tasklist.DoesNotExist: 
            return JsonResponse({'message': ' Tasklist not found.'}, status=404) 
        
        task = Task(tasklist=tasklist, title=data['title'] , description=data['description'], completed=data['completed'], watch=data['watch'], due_date=data['due_date'], due_time=data['due_time'], order=data['order'])

        try: 
            task.save()  
        except Exception as error:
            logging.error(error)
            return JsonResponse({'message': 'Error when saving'}, status=500) 
        
        return JsonResponse({"message": 'Task created'}, status=201)


@csrf_exempt
@require_http_methods(["GET","PUT", "PATCH" ,"DELETE"])
def task_id(request, task_id):
    if request.method == "GET":
        try:
            task = Task.objects.get(id=task_id)
            single_task = model_to_dict(task)
        except Task.DoesNotExist: 
            return JsonResponse({'message': ' Task not found.'}, status=404)    
        
        return JsonResponse(single_task, safe=False)      
    elif request.method in ("PUT", "PATCH"):

        data = json.loads(request.body)

        try:
            Task.objects.filter(id=task_id).update(**data)
        except IntegrityError:
            return JsonResponse({'message': ' Task not found.'}, status=404)

        return JsonResponse({"message": 'Task updated'}, status=200)
        
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
    except Task.DoesNotExist:
        return JsonResponse({'message': ' Task not found.'}, status=404) 

    return JsonResponse({"message": 'Task deleted'}, status=200) 
         


# Tasklists
# GET /tasklists/ - retorna todas as tasklists -  ✅
# GET /tasklists/:id/ - retorna apenas uma tasklist ✅ 
# POST /tasklists/ - cria uma nova tasklist ✅
# PUT/PATCH /tasklists/:id/ - atualiza apenas uma tasklist ✅
# DELETE /tasklists/:id/ - deleta apenas uma tasklist ✅

# Tasks
# GET /tasklists/:id/tasks/ - retorna todas as tasks de uma determinada tasklist ✅
# GET /tasklists/:id/tasks/:id - retorna apenas uma task dentre as tasks de uma determinada tasklist 
# POST /tasklists/:id/tasks/ - cria uma nova task✅
# PUT/PATCH? /tasks/:id/ - atualiza apenas uma task de uma determinada tasklist
# DELETE /tasks/:id/ - deleta apenas uma task✅




