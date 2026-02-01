from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def taskslist(request):
    tasks = Task.objects.all()
    return render(request, "Tasks/list.html", {"tasks": tasks})

def createtask(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save()
        return redirect("Tasks:TasksList")
    return render(request, "Tasks/formulaire.html", {"form": form})
