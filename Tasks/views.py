from django.shortcuts import render, redirect, get_object_or_404
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

def deletetask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("Tasks:TasksList")

def updatetask(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("Tasks:TasksList")
    return render(request, "Tasks/formulaire.html", {"form": form})