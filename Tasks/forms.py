from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        Model = Task
        fields = ['titre', 'description']