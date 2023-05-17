
from django.urls import resolve
from django.test import TestCase
from User_App.views import login_page, register_page
from .forms import UserLoginForm, UserRegisterForm


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


class RegisterPageTest(TestCase):

    def test_url_resolves_to_register_page_view(self):
        found = resolve('/register')
        self.assertEqual(found.func, register_page)

    def test_register_page_template(self):
        response = self.client.get('/register')
        self.assertTemplateUsed(response, 'register.html')

    def test_register_page_form_rendering(self):
        form_data = {'username': 'something1',
                     'first_name': 'something2',
                     'last_name': 'something3',
                     'email': 'something4'}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
