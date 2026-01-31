from django.shortcuts import render, redirect
from .models import Task

def taskslist(request):
    tasks = Task.objects.all()
    return render(request, "Tasks/list.html", {"tasks": tasks})
