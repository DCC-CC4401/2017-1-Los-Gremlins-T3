from django.shortcuts import render
from django.contrib.auth.models import User
from user.models import AbstractUser, Seller, WalkingSeller, FixedSeller, PaymentMethod
from django.core.exceptions import ObjectDoesNotExist
import datetime


def fichavendedor(request, id):
    try:
        # find django user with that id.
        context = {}
        context['now'] = datetime.datetime.now()
        duser = User.objects.get(pk=id)
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



def check_active(start_hour, end_hour):
    return True
