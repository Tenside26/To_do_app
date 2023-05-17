
from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40, label="Username", widget=forms.TextInput)
    password = forms.CharField(max_length=40, label="Password", widget=forms.PasswordInput)
