from django.test import TestCase
from .factories import TaskFactory, TaskListFactory, UserFactory
from pytest_factoryboy import register

register(TaskFactory)
register(TaskListFactory)
register(UserFactory)


class TaskListTest(TestCase):
    pass


class TaskTest(TestCase):

    def test_str_return(self, task_factory):
        task = task_factory(title="new-title")
        assert task.__str__() == "new-title"
