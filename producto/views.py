from django.shortcuts import render
from producto.models import Producto
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def producto(request, pkid):
    try:
        page = Producto.objects.get(pk=pkid)
        context = { 'page': page }
    except ObjectDoesNotExist:
        context = None
    return render(request, 'gremlins/gestion-productos.html', context)
