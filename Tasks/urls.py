from django.urls import path
from Tasks import views

app_name = "Tasks"

urlpatterns = [
    path('', views.taskslist, name='TasksList'),
    path('create/', views.createtask, name='CreateTask'),
    # path('update/<int:pk>/', views.updatetask, name='UpdateTask'),
    # path('delete/<int:pk>/', views.deletetask, name='DeleteTask'),
]