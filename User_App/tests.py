
from django.urls import resolve
from django.test import TestCase
from User_App.views import login_page


class LoginPageTest(TestCase):

    def test_url_resolves_to_login_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, login_page)

    def test_login_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'login.html')
