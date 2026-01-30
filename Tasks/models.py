from django.db import models

class Task(models.Model):
    titre = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"