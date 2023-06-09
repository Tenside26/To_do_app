
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login


def login_page(request):

    template = "login.html"
    form = UserLoginForm

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("main")

    return render(request, template, {"form": form})


def register_page(request):

    template = "register.html"
    form = UserRegisterForm

    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, template, {"form": form})
