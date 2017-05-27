from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from user.forms import SignUpForm

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


from django.contrib.auth.models import User



def signup(request):

    if request.method == 'POST':
        userPass = request.POST.get('password', None)
        userMail = request.POST.get('email', None)

        if userMail and userPass:

            u, created = User.objects.get_or_create(userMail, userMail)
            if created:
                u.set_password(userPass)
                u.save()
                return render(request, 'profile.html', {u})
            else:
                return render(request, 'profile.html', {u})
        else:
            return render(request, 'home.html')

    else:
        form = SignUpForm()
        return render(request, 'user/signup.html', {'form': form})


    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user:login')
        return render(request, 'user/signup.html', {'form': form})
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