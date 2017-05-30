from django.shortcuts import render, redirect
from producto.models import Producto
from django.core.exceptions import ObjectDoesNotExist
from producto.forms import CreateProductoForm, EditProductoForm
from producto.models import Producto
from user.models import AbstractUser, Seller
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def add_producto(request):
    if not request.user.is_authenticated:
        return redirect('not-found.html')
    try:
        duser = request.user
        auser = AbstractUser.objects.get(user=duser)
        seller = Seller.objects.get(user=auser)
        if request.method == 'POST':
            print("post")
            form = CreateProductoForm(request.POST)
            if form.is_valid():
                print('saving')
                producto = Producto(
                    name=form.cleaned_data['name'],
                    price=form.cleaned_data['price'],
                    stock=form.cleaned_data['stock'],
                    description=form.cleaned_data['description'],
                    category=form.cleaned_data['category'],
                    owner=seller,
                    #photo=form.cleaned_data['img'],
                    prev_img_id=form.cleaned_data['prev_img']
                )
                producto.save()
            return redirect('/ficha_vendedor/' + str(duser.id))
        else:
            form = CreateProductoForm()
        return render(request, 'producto/add-product.html', {'form': form, 'uid': duser.id})
    except ObjectDoesNotExist:
        return redirect('not-found.html')



def producto(request, pkid):
    print('edittt')
    if not request.user.is_authenticated:
        return redirect('not-found.html')
    try:
        print('got producto')
        product = Producto.objects.get(pk=pkid)
        duser = request.user
        auser = AbstractUser.objects.get(user=duser)
        context = {'page': product, 'pk':pkid}
    except ObjectDoesNotExist:
        return redirect('not-found.html')
    if request.method == 'POST':
        print("post!")
        form = EditProductoForm(request.POST)
        if form.is_valid():
            print("valid!")
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            stock = form.cleaned_data['stock']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            prev_img_id = form.cleaned_data['prev_img']

            print(name)
            if name is not "":
                print("edited name")
                product.name = name
            if price is not None:
                print("edited price")

                product.price = price
            if stock is not None:
                print("edited stock")
                product.stock = stock
            if description is not "":
                print("edited description")
                product.description = description
            if category is not "":
                print("edited category")
                product.category = category
            if prev_img_id is not "":
                print("edited prev_img_id")
                product.prev_img_id = prev_img_id
            product.save()
        return redirect('/ficha_vendedor/' + str(product.owner.user.user.id))

    else:
        form = EditProductoForm(initial={'name':product.name,
                                         'price':product.price,
                                         'stock':product.stock,
                                         'description':product.description,
                                         'category':product.category,
                                         'prev_img': product.prev_img_id})
        context['form'] = form
        if auser.account_type == 4:
            return render(request, 'producto/edit-product.html', context)
        try:
            seller = Seller.objects.get(user=auser)
            if product.owner.id == seller.id:
                return render(request, 'producto/edit-product.html', context)
        except ObjectDoesNotExist:
            pass
    return redirect('not-found.html')


def delete_producto(request, pkid):
    try:
        product = Producto.objects.get(pk=pkid)
    except ObjectDoesNotExist:
        return render(request, 'not-found.html')
    if request.user.is_authenticated():
        logged_user = AbstractUser.objects.get(user=request.user)
        if logged_user.account_type is 4:
            # admin
            product.delete()
            return redirect('/ficha_vendedor/' + str(product.owner.user.user.id))
        try:
            seller = Seller.objects.get(user=logged_user)
            if product.owner.id == seller.id:
                product.delete()
                return redirect('/ficha_vendedor/' + str(product.owner.user.user.id))
        except ObjectDoesNotExist:
            pass
    return render(request, 'not-found.html')


