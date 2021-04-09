from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    profiles = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    context = {
        'profiles': profiles,
    }
    return render(request, "home.html", context)
