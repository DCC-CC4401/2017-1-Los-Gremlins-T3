from django.http import HttpResponse
from django.shortcuts import render


def gestionproductos(request):
    return render(request, 'gestion-productos.html', {})

