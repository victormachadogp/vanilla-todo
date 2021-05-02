from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasklists/', views.tasklists),
    path('tasklists/<int:tasklist_id>/', views.tasklistsid),
    path('tasklists/<int:tasklist_id>/tasks', views.tasklists_id_tasks),
    path('task/<int:task_id>', views.task_id)
]
