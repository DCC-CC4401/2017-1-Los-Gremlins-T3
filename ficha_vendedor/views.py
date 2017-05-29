from django.shortcuts import render
from django.contrib.auth.models import User
from user.models import AbstractUser, Seller, WalkingSeller, FixedSeller, PaymentMethod, Student
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from ficha_vendedor.forms import FixedSellerEditForm, WalkingSellerEditForm
from ficha_vendedor.utils import check_fixed_seller_active

import datetime


def fichavendedor(request, pkid):
    try:
        duser = User.objects.get(pk=pkid)
        auser = AbstractUser.objects.get(user=duser)
        # find django user with that id.
        context = {}
        context['pkid'] = pkid
        context['now'] = datetime.datetime.now()
        context['auser'] = auser
        if auser.account_type is 2:
            # walking seller
            seller = Seller.objects.get(user=auser)
            context['seller'] = seller
            walking_seller = WalkingSeller.objects.get(super_seller=seller)
            context['walking_seller'] = walking_seller
            if request.user.is_authenticated() and request.user.id == int(pkid):
                # Vista del vendedor
                return render(request, 'ficha_vendedor/vendedor-ambulante-profile.html', context)
            else:
                # Vista del estudiante
                logged_auser = AbstractUser.objects.get(user=request.user)
                if logged_auser.account_type is 1:
                    # Es estudiante
                    logged_student = Student.objects.get(user=logged_auser)
                    print('es estudiante')
                    if seller in logged_student.favorites.all():
                        print('es fav')
                        context['is_favorited'] = True
                        if request.method == 'POST':
                            # switch behaviour
                            context['is_favorited'] = False
                            logged_student.favorites.remove(seller)
                            logged_student.save()
                            seller.times_favorited -= 1
                            seller.save()
                    else:
                        if request.method == 'POST':
                            print('se hace fav')
                            context['is_favorited'] = True
                            logged_student.favorites.add(seller)
                            logged_student.save()
                            seller.times_favorited += 1
                            seller.save()

                return render(request, 'ficha_vendedor/vendedor-ambulante-public.html', context)
        elif auser.account_type is 3:
            # fixed seller
            seller = Seller.objects.get(user=auser)
            context['seller'] = seller
            fixed_seller = FixedSeller.objects.get(super_seller=seller)
            context['fixed_seller'] = fixed_seller
            context['avaialble'] = check_fixed_seller_active(fixed_seller.start_hour, fixed_seller.end_hour)
            # check if it available
            datetime.datetime.now()
            if request.user.is_authenticated() and request.user.id == int(pkid):
                # Vista del vendedor
                return render(request, 'ficha_vendedor/vendedor-fijo-profile.html', context)
            else:
                # Vista del estudiante
                logged_auser = AbstractUser.objects.get(user=request.user)
                if logged_auser.account_type is 1:
                    # Es estudiante
                    logged_student = Student.objects.get(user=logged_auser)
                    print('es estudiante')
                    if seller in logged_student.favorites.all():
                        print('es fav')
                        context['is_favorited'] = True
                        if request.method == 'POST':
                            # switch behaviour
                            context['is_favorited'] = False
                            logged_student.favorites.remove(seller)
                            logged_student.save()
                            seller.times_favorited -= 1
                            seller.save()
                    else:
                        if request.method == 'POST':
                            print('se hace fav')
                            context['is_favorited'] = True
                            logged_student.favorites.add(seller)
                            logged_student.save()
                            seller.times_favorited += 1
                            seller.save()
                return render(request, 'ficha_vendedor/vendedor-fijo-public.html', context)
    except ObjectDoesNotExist:
        return render(request, 'not-found.html')
    return render(request, 'not-found.html')


def seller_edit(request, pkid):
    duser = User.objects.get(pk=pkid)
    auser = AbstractUser.objects.get(user=duser)
    if auser.account_type is 2:
        # walking seller
        return walking_seller_edit(request, pkid)
    elif auser.account_type is 3:
        # fixed seller
        return fixed_seller_edit(request, pkid)
    return render(request, 'not-found.html')


def fixed_seller_edit(request, pkid):
    try:
        duser = User.objects.get(pk=pkid)
        auser = AbstractUser.objects.get(user=duser)
        seller = Seller.objects.get(user=auser)
        fixed_seller = FixedSeller.objects.get(super_seller=seller)
    except ObjectDoesNotExist:
        return render(request, 'not-found.html')
    if request.method == 'POST':
        form = FixedSellerEditForm(request.POST)
        if form.is_valid() and form.pass_is_valid():  # should show me pass dont match
            email = form.cleaned_data['email']
            fullname = form.cleaned_data['fullname']
            pay_methods = form.cleaned_data['pay_methods']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            start_hour = form.cleaned_data['start_hour']
            end_hour = form.cleaned_data['end_hour']

            if email is not "":
                print('changed mail')
                duser.email = email
                duser.username = email
                duser.save()
            if fullname is not "":
                print('changed fullname')
                auser.fullname = fullname
                auser.save()
            if password is not "":
                print('changed pass')
                duser.set_password(password)
                duser.save()
            if pay_methods is not None:
                print('changed pay')
                seller.payment_methods.clear()
                seller.payment_methods.add(pay_methods)
                seller.save()
            if start_hour is not None:
                print('changed start hour')
                fixed_seller.start_hour = start_hour
            if end_hour is not None:
                print('changed end hour')
                fixed_seller.end_hour = end_hour
            if address is not "":
                print('changed address')
                fixed_seller.address = address
            fixed_seller.save()
            return redirect('ficha_vendedor/'+str(pkid))
    else:
        logged_auser = AbstractUser.objects.get(user=request.user)
        print(str(logged_auser.account_type))
        if request.user.is_authenticated() and \
                ((request.user.id == int(pkid) and auser.account_type is 2) or logged_auser.account_type is 4):
            form = FixedSellerEditForm({})  # TODO: Preload with previous data
            return render(request, 'ficha_vendedor/vendedor-edit.html', {'form': form, 'pkid': pkid})
        return render(request, 'not-found.html')


def walking_seller_edit(request, pkid):
    try:
        duser = User.objects.get(pk=pkid)
        auser = AbstractUser.objects.get(user=duser)
        seller = Seller.objects.get(user=auser)
    except ObjectDoesNotExist:
        return render(request, 'not-found.html')
    if request.method == 'POST':
        form = WalkingSellerEditForm(request.POST)
        if form.is_valid() and form.pass_is_valid():  # should show me pass dont match
            email = form.cleaned_data['email']
            fullname = form.cleaned_data['fullname']
            pay_methods = form.cleaned_data['pay_methods']
            password = form.cleaned_data['password']

            if email is not "":
                print('changed mail')
                duser.email = email
                duser.username = email
                duser.save()
            if fullname is not "":
                print('changed fullname')
                auser.fullname = fullname
                auser.save()
            if password is not "":
                print('changed pass')
                duser.set_password(password)
                duser.save()
            if pay_methods is not None:
                print('changed pay')
                seller.payment_methods.clear()
                seller.payment_methods.add(pay_methods)
                seller.save()
            return redirect('ficha_vendedor/' + str(pkid))
    else:
        logged_auser = AbstractUser.objects.get(user=request.user)
        print(str(logged_auser.account_type))

        if request.user.is_authenticated() and \
                ((request.user.id == int(pkid) and auser.account_type is 2) or logged_auser.account_type is 4):
            form = WalkingSellerEditForm({})  # TODO: Preload with previous data
            return render(request, 'ficha_vendedor/vendedor-edit.html', {'form': form, 'pkid': pkid})
    return render(request, 'not-found.html')


def checkin(request):
    if request.user.is_authenticated():
        auser = AbstractUser.objects.get(user=request.user)
        if auser.account_type is 2:
            seller = Seller.objects.get(user=auser)
            walking_seller = WalkingSeller.objects.get(super_seller=seller)
            if walking_seller.is_active:
                walking_seller.is_active = False
            else:
                walking_seller.is_active = True
            walking_seller.save()
            return redirect('ficha_vendedor/' + str(request.user.id))


def delete_seller(request, pkid):
    try:
        duser = User.objects.get(pk=pkid)
        auser = AbstractUser.objects.get(user=duser)
        seller = Seller.objects.get(user=auser)
        walking_seller = None
        fixed_seller = None
        if auser.account_type is 2:
            walking_seller = WalkingSeller.objects.get(super_seller=seller)
        elif auser.account_type is 3:
            fixed_seller = FixedSeller.objects.get(super_seller=seller)
    except ObjectDoesNotExist:
        return render(request, 'not-found.html')
    if request.user.is_authenticated():
        print('auth')
        logged_user = AbstractUser.objects.get(user=request.user)
        if logged_user.account_type is 4:
            print('admin')
            # admin
            if walking_seller:
                walking_seller.delete()
            if fixed_seller:
                fixed_seller.delete()
            seller.delete()
            auser.delete()
            duser.delete()
            return redirect('index')
    return render(request, 'not-found.html')
