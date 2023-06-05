from django.test import TestCase
from .factories import TaskFactory, TaskListFactory, UserFactory
from pytest_factoryboy import register
import factory
from django.db.models import signals
import datetime
from django.contrib.auth.models import User


register(TaskFactory)
register(TaskListFactory)
register(UserFactory)


class UserTest(TestCase):

    def test_user_model(self):
        with factory.django.mute_signals(signals.post_save):
            user = UserFactory()
            assert isinstance(user.username, str)
            assert isinstance(user.password, str)
            assert isinstance(user.first_name, str)
            assert isinstance(user.last_name, str)
            assert isinstance(user.email, str)


class TaskTest(TestCase):

    def test_task_model(self):
        with factory.django.mute_signals(signals.post_save):
            task = TaskFactory()
            assert isinstance(task.title, str)
            assert isinstance(task.description, str)
            assert isinstance(task.creation_date, datetime.datetime)
            assert isinstance(task.completed, bool)


class TaskListTest(TestCase):

    def test_task_list_model(self):
        with factory.django.mute_signals(signals.post_save):
            task_list = TaskListFactory()
            assert isinstance(task_list.owner, User)

