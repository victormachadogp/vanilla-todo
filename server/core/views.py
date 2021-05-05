import json

from django.db.utils import IntegrityError
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse 
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Tasklist, Task


@require_http_methods(["GET","POST"]) 
def tasklists(request):
    try: 
        tasks = Tasklist.objects.all().values()
    except Tasklist.DoesNotExist: 
        return JsonResponse({'message': 'Tasklists do not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        task_list = list(tasks)  
        return JsonResponse(task_list, safe=False)
    else:
        return HttpResponse("POST")    


@csrf_exempt
@require_http_methods(["PUT", "GET", "DELETE"])
def tasklistsid(request, tasklist_id):
    try: 
        tasklist = Tasklist.objects.get(id=tasklist_id)     
    except Tasklist.DoesNotExist: 
        return JsonResponse({'message': 'Tasklist_id does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == "GET":
        return JsonResponse(model_to_dict(tasklist), safe=False)

    elif request.method == "PUT" or request.method == "PATCH":
        
        data = json.loads(request.body)
 
        try:
            Tasklist.objects.filter(id=tasklist_id).update(**data) 
        except IntegrityError: 
            return HttpResponse('ERRO - Id é invalido', status=404) 
       
        return HttpResponse('OK', status=200)
    
    elif request.method == "DELETE":
        tasklist.delete()
        return JsonResponse({'mesage': 'Tasklist foi deletada!'}, status=204)


#TASKS
@require_http_methods(["GET"]) 
def tasklists_id_tasks(request, tasklist_id):
    tasks = Task.objects.filter(tasklist=tasklist_id).values()
    return JsonResponse(list(tasks), safe=False)

# Tasklists
# GET /tasklists/ - retorna todas as tasklists -  ✅
# GET /tasklists/:id/ - retorna apenas uma tasklist ✅ 
# POST /tasklists/ - cria uma nova tasklist 
# PUT/PATCH /tasklists/:id/ - atualiza apenas uma tasklist ✅
# DELETE /tasklists/:id/ - deleta apenas uma tasklist ✅

# Tasks
# GET /tasklists/:id/tasks/ - retorna todas as tasks de uma determinada tasklist ✅
# POST /tasklists/:id/tasks/ - cria uma nova task
# PUT/PATCH? /tasks/:id/ - atualiza apenas uma task de uma determinada tasklist
# DELETE /tasks/:id/ - deleta apenas uma task



