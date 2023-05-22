
from django.urls import resolve, reverse
from django.test import TestCase
from User_App.views import login_page, register_page
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User


class LoginPageTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='something1', password='something2')

    def test_url_resolves_to_login_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, login_page)

    def test_login_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'login.html')

    def test_login_page_form_password_validation_with_correct_password(self):
        form_data = {'username': 'something1',
                     'password': 'something2'}
        form = UserLoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_page_form_password_validation_with_wrong_password(self):
        form_data = {'username': 'something1',
                     'password': 'something3'}
        form = UserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_hyperlink_to_register_page(self):
        response = self.client.get("/")
        self.assertContains(response, '<a href="%s"><button>Click</button></a>' % reverse("register"), html=True)


class RegisterPageTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='something1',
                                 password='asxd123zxc',
                                 email='something3@gmail.com')

    def test_url_resolves_to_register_page_view(self):
        found = resolve('/register')
        self.assertEqual(found.func, register_page)

    def test_register_page_template(self):
        response = self.client.get('/register')
        self.assertTemplateUsed(response, 'register.html')

    def test_register_page_form_email_validation_with_existing_email(self):
        form_data = {'username': 'something11',
                     'password1': "asd123zxc",
                     'password2': "asd123zxc",
                     'first_name': 'something22',
                     'last_name': 'something33',
                     'email': 'something3@gmail.com'}
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_page_form_email_validation_with_nonexistent_email(self):
        form_data = {'username': 'something11',
                     'password1': "asd123zxc",
                     'password2': "asd123zxc",
                     'first_name': 'something22',
                     'last_name': 'something33',
                     'email': 'something4@gmail.com'}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_page_form_username_validation_with_existing_username(self):
        form_data = {'username': 'something1',
                     'password1': "asd123zxc",
                     'password2': "asd123zxc",
                     'first_name': 'something22',
                     'last_name': 'something33',
                     'email': 'something4@gmail.com'}
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_page_form_username_validation_with_nonexistent_username(self):
        form_data = {'username': 'something11',
                     'password1': "asd123zxc",
                     'password2': "asd123zxc",
                     'first_name': 'something22',
                     'last_name': 'something33',
                     'email': 'something4@gmail.com'}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_hyperlink_to_login_page(self):
        response = self.client.get("/register")
        self.assertContains(response, '<a href="%s"><button>Click</button></a>' % reverse("login"), html=True)






