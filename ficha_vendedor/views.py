from django.shortcuts import render


def fichavendedor(request):
    return render(request, 'vendedor-profile-page.html', {})