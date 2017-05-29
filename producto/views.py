from django.shortcuts import render
from producto.models import Producto
from django.core.exceptions import ObjectDoesNotExist
from producto.forms import CreateProductoForm
from producto.models import Producto

# Create your views here.

def producto(request, pkid):
    try:
        page = Producto.objects.get(pk=pkid)
        context = { 'page': page }
    except ObjectDoesNotExist:
        context = {}

    if request.method == 'POST':
        form = CreateProductoForm(request.POST)
        if form.is_valid():
            producto = Producto.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
                description=form.cleaned_data['description'],
                owner=1,
                photo=form.cleaned_data['img'],
                prev_img_id=form.cleaned_data['prev_img']
            )
    else:
        form = CreateProductoForm()

    context['form'] = form
    return render(request, 'producto/gestion-productos.html', context)
