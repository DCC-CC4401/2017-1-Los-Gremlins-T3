from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
#
# def create(request):
#     if request.method == "POST":
#         firstname = request.POST.get('firstname', '')
#         lastname = request.POST.get('lastname', '')
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         password2 = request.POST.get('password2', '')
#         email = request.POST.get('email', '')
#
#         if firstname == "" or lastname == "" or username == "" or password == "" or password2 == "" or email == "" or password != password2:
#             template = loader.get_template('user/create.html')
#             context = {"error": True}
#             return HttpResponse(template.render(context, request))
#         else:
#             user = User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
#             # Create the stoner user
#             stoner = Stoner(user=user)
#             stoner.save()
#             context = {'registered': True}
#             return render(request, 'user/login.html', context)
#
#     else:
#         template = loader.get_template('user/create.html')
#         context = {}
#         return HttpResponse(template.render(context, request))
#

def login(request):
    if "logged_in" in request.session and request.session["logged_in"]:
        return redirect('user:index')
    return render(request, 'user/login.html', {})


def signup(request):
    return render(request, 'user/signup.html', {})


# def logout(request):
#     try:
#         auth_logout(request)
#         del request.session['logged_in']
#         del request.session['username']
#     except KeyError:
#         pass
#     return redirect('homepage:index')