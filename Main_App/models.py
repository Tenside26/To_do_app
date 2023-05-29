from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    title = models.CharField(max_length=80)
    description = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)


class TaskList(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="task_list_owner")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task")



