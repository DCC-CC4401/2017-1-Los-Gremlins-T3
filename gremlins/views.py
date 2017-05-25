from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'gremlins/index.html', {})

def login(request):
    return render(request, 'gremlins/login.html', {})

def signup(request):
    return render(request, 'gremlins/signup.html', {})

def user(request):
    return render(request, 'gremlins/vendedor-profile-page.html', {})

def gestionproductos(request):
    return render(request, 'gremlins/gestion-productos.html', {})
