
from django.shortcuts import render


def main_page(request):

    template = "main.html"

    return render(request, template)
