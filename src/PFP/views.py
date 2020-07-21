from django.shortcuts import render, redirect
from django.http import HttpResponse
from src.home.models import Students


def homepage(request):
    return render(request, "homepage.html")


def news(request):
    return render(request, "news.html")


def about(request):
    return render(request, "about.html")
