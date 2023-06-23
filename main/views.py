from django.shortcuts import render
from django.http import HttpResponse


def start(request):
    return render(request, 'main/base.html')

def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')





