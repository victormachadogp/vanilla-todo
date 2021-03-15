from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasklists/', views.tasklists),
    path('tasklists/<int:tasklist_id>/', views.tasklistsid)
]
