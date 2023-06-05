import factory
from django.contrib.auth.models import User
from .models import Task, TaskList
from django.utils import timezone


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "placeholder"
    password = "placeholder"
    first_name = "placeholder"
    last_name = "placeholder"
    email = "placeholder@gmail.com"


class TaskListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskList

    owner = factory.SubFactory(UserFactory)


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = "placeholder"
    description = "placeholder"
    creation_date = timezone.now
    completed = False
    task_list = factory.SubFactory(TaskListFactory)
