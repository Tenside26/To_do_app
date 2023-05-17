
from django import forms
from django.contrib.auth.forms import UserCreationForm, User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40, label="Username", widget=forms.TextInput)
    password = forms.CharField(max_length=40, label="Password", widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]
