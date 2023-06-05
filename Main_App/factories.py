import factory
from django.contrib.auth.models import User
from .models import Task, TaskList
from faker import Faker


fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.word()
    password = fake.password()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()


class TaskListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskList

    owner = factory.SubFactory(UserFactory)


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = fake.sentence(nb_words=2)
    description = fake.sentence(nb_words=20)
    creation_date = fake.date()
    completed = fake.boolean()
    task_list = factory.SubFactory(TaskListFactory)
