from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'gremlins/index.html', {})

def gestionproductos(request):
    return render(request, 'gremlins/gestion-productos.html', {})
