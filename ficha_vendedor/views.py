from django.shortcuts import render
from django.contrib.auth.models import User
from user.models import AbstractUser, Seller, WalkingSeller, FixedSeller, PaymentMethod
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from ficha_vendedor.forms import FixedSellerEditForm, WalkingSellerEditForm

import datetime


def fichavendedor(request, pkid):
    try:
        # find django user with that id.
        context = {}
        context['now'] = datetime.datetime.now()
        duser = User.objects.get(pk=pkid)
        auser = AbstractUser.objects.get(user=duser)
        context['auser'] = auser
        if auser.account_type is 2:
            # walking seller
            seller = Seller.objects.get(user=auser)
            context['seller'] = seller
            walking_seller = WalkingSeller.objects.get(super_seller=seller)
            context['walking_seller'] = walking_seller
            return render(request, 'ficha_vendedor/vendedor-ambulante-profile.html', context)
        elif auser.account_type is 3:
            # fixed seller
            seller = Seller.objects.get(user=auser)
            context['seller'] = seller
            fixed_seller = FixedSeller.objects.get(super_seller=seller)
            context['fixed_seller'] = fixed_seller
            context['avaialble'] = check_active(fixed_seller.start_hour, fixed_seller.end_hour)
            # check if it available
            datetime.datetime.now()
            return render(request, 'ficha_vendedor/vendedor-fijo-profile.html', context)

        return render(request, 'ficha_vendedor/not-found.html')
    except ObjectDoesNotExist:
        return render(request, 'ficha_vendedor/not-found.html')


def seller_edit(request,pkid):
    duser = User.objects.get(pk=pkid)
    auser = AbstractUser.objects.get(user=duser)
    if auser.account_type is 2:
        # walking seller
        return walking_seller_edit(request, pkid)
    elif auser.account_type is 3:
        # fixed seller
        return fixed_seller_edit(request, pkid)
    return render(request, 'ficha_vendedor/not-found.html')


def fixed_seller_edit(request, pkid):
    if request.method == 'POST':
        form = FixedSellerEditForm(request.POST)
        try:
            duser = User.objects.get(pk=pkid)
            auser = AbstractUser.objects.get(user=duser)
            seller = Seller.objects.get(user=auser)
            fixed_seller = FixedSeller.objects.get(super_seller=seller)
        except ObjectDoesNotExist:
            return render(request, 'ficha_vendedor/not-found.html')

        if form.is_valid() and form.pass_is_valid():  # should show me pass dont match
            email = form.cleaned_data['email']
            pay_methods = form.cleaned_data['pay_methods']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            start_hour = form.cleaned_data['start_hour']
            end_hour = form.cleaned_data['end_hour']

            if email is not None:
                duser.email = email
                duser.username = email
                duser.save()
            if password is not None:
                duser.set_password(password)
                duser.save()
            if pay_methods is not None:
                seller.payment_methods.clear()
                seller.payment_methods.add(pay_methods)
                seller.save()
            if start_hour is not None:
                fixed_seller.start_hour = start_hour
            if end_hour is not None:
                fixed_seller.end_hour = end_hour
            if address is not None:
                fixed_seller.address = address
            fixed_seller.save()

            return redirect('login')
    else:
        form = FixedSellerEditForm({}) # TODO: Preload with previous data
    return render(request, 'ficha_vendedor/vendedor-edit.html', {'form': form, 'pkid': pkid})


def walking_seller_edit(request, pkid):
    if request.method == 'POST':
        form = WalkingSellerEditForm(request.POST)
        try:
            duser = User.objects.get(pk=pkid)
            auser = AbstractUser.objects.get(user=duser)
            seller = Seller.objects.get(user=auser)
            walking_seller = WalkingSeller.objects.get(super_seller=seller)
        except ObjectDoesNotExist:
            return render(request, 'ficha_vendedor/not-found.html')

        if form.is_valid() and form.pass_is_valid():  # should show me pass dont match
            email = form.cleaned_data['email']
            pay_methods = form.cleaned_data['pay_methods']
            password = form.cleaned_data['password']

            if email is not None:
                duser.email = email
                duser.username = email
                duser.save()
            if password is not None:
                duser.set_password(password)
                duser.save()
            if pay_methods is not None:
                seller.payment_methods.clear()
                seller.payment_methods.add(pay_methods)
                seller.save()
            return redirect('login')
    else:
        form = WalkingSellerEditForm({}) # TODO: Preload with previous data
    return render(request, 'ficha_vendedor/vendedor-edit.html', {'form': form, 'pkid': pkid})

def check_active(start_hour, end_hour):
    return True
