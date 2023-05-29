from django.contrib import admin
from .models import Task, TaskList


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "creation_date", "completed"]


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ["owner"]
