from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'gremlins/index.html', {})

def vendedorProfile(request):
    return render(request, 'gremlins/vendedor-profile-page.html', {})

