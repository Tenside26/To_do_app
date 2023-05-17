
from django.urls import resolve
from django.test import TestCase
from User_App.views import login_page
from .forms import UserLoginForm


class LoginPageTest(TestCase):

    def test_url_resolves_to_login_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, login_page)

    def test_login_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'login.html')

    def test_login_page_form_rendering(self):
        form_data = {'username': 'something1',
                     'password': 'something2'}
        form = UserLoginForm(data=form_data)
        self.assertTrue(form.is_valid())
