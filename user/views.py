from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from user.forms import SignUpForm
from django.contrib.auth.models import User
from user.models import AbstractUser

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



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() and form.pass_is_valid(): # should show me pass dont match
            account_type = form.cleaned_data['account_type']
            duser = User.objects.create_superuser(form.cleaned_data['email'],
                                                  form.cleaned_data['email'],
                                                     form.cleaned_data['password'])

            auser = AbstractUser(user=duser, fullname=form.cleaned_data['fullname'])
            auser.save()

            return render(request, 'user/signup2.html', {'duser': duser, 'auser': auser, 'type': account_type})
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


# def logout(request):
#     try:
#         auth_logout(request)
#         del request.session['logged_in']
#         del request.session['username']
#     except KeyError:
#         pass
#     return redirect('homepage:index')