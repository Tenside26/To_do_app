
from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40, label="Username", widget=forms.TextInput)
    password = forms.CharField(max_length=40, label="Password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Username does not exists")
            if not user.check_password(password):
                raise forms.ValidationError("Wrong Password")


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")
        return username

    def clean(self):
        form_data = self.cleaned_data
        if form_data.get('password1') != form_data.get('password2'):
            self.errors.get["password1"] = ["Password do not match"]
            del form_data['password1']
        return form_data
