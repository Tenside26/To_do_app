from django.db import models


class TaskList(models.Model):
    # Models Still in Progress
    task_list_owner = #ForeignKey To User
    task_list_item =#ManyToMany To Task

class Task(models.Model):
    # Models Still in Progress
    task_user = # Potential User Who Added That Task
    task_title = models.CharField(max_length=80)
    task_description = models.TextField(max_length=1000)
    task_creation_date = models.DateTimeField(auto_now_add=True)



