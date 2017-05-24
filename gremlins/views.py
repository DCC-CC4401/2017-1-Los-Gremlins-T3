from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'gremlins/index.html', {})

def login(request):
    return render(request, 'gremlins/login.html', {})
