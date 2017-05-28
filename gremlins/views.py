from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def gestionproductos(request):
    return render(request, 'gestion-productos.html', {})

def fichavendedor(request):
    return render(request, 'vendedor-profile-page.html', {})

