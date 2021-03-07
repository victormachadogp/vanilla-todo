from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from .models import Tasklist
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.

@require_http_methods(["GET","POST"]) 
def get_tasklists(request):
    try: 
        tasks = Tasklist.objects.all().values()  
    except Tasklists.DoesNotExist: 
        return JsonResponse({'message': 'Tasklists do not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == "GET":
        task_list = list(tasks)  
        return JsonResponse(task_list, safe=False)
    else:
        return HttpResponse("POST")    


@require_http_methods(["PUT","DELETE","GET"])
def get_tasklistsid(request, tasklist_id):
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
# POST /tasklists/ - cria uma nova tasklist 
# PUT/PATCH? /tasklists/:id/ - atualiza apenas uma tasklist
# DELETE /tasklists/:id/ - deleta apenas uma tasklist

# Tasks
# GET /tasklists/:id/tasks/ - retorna todas as tasks de uma determinada tasklist
# POST /tasklists/:id/tasks/ - cria uma nova task
# PUT/PATCH? /tasks/:id/ - atualiza apenas uma task de uma determinada tasklist
# DELETE /tasks/:id/ - deleta apenas uma task



