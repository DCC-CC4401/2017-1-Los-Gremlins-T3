from django.shortcuts import render


def fichavendedor(request, id):
    return render(request, 'ficha_vendedor/vendedor-profile-page.html', {'id': id})