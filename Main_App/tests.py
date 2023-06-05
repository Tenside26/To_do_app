from django.test import TestCase
from .factories import TaskFactory, TaskListFactory, UserFactory
from pytest_factoryboy import register
import factory
from django.db.models import signals


register(TaskFactory)
register(TaskListFactory)
register(UserFactory)


class TaskListTest(TestCase):

    def test_task_list_model(self):
        with factory.django.mute_signals(signals.post_save):
            task_list = TaskListFactory()
            assert task_list.owner == UserFactory()


class TaskTest(TestCase):

    def test_task_model(self):
        with factory.django.mute_signals(signals.post_save):
            task = TaskFactory()
            assert task.title == "placeholder"
            assert task.description == "placeholder"
            assert task.completed is False
