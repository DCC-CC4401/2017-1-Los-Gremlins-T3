from user.models import AbstractUser, Student, Seller, WalkingSeller, FixedSeller
from django.core.exceptions import ObjectDoesNotExist


def user_processor(request):

    auser = None
    seller = None

    dict = {}
    dict['logged_auth'] = False


    if request.user.is_authenticated():
        user = request.user
        dict['logged_user'] = user
        try:
            auser = AbstractUser.objects.get(user=user)
            dict['logged_abstract_user'] = auser
            dict['logged_auth'] = True
            dict['logged_name'] = auser.fullname
            dict['logged_avatar'] = auser.avatar
        except ObjectDoesNotExist:
            pass

        try:
            seller = Seller.objects.get(user=auser)
            dict['logged_seller'] = seller
        except ObjectDoesNotExist:
            pass

        try:

            student = Student.objects.get(user=auser)
            dict['logged_student'] = student
        except ObjectDoesNotExist:
            pass

        try:
            walking_seller = WalkingSeller.objects.get(super_seller=seller)
            dict['logged_walking_seller'] = walking_seller
        except ObjectDoesNotExist:
            pass

        try:
            fixed_seller = FixedSeller.objects.get(super_seller=seller)
            dict['logged_fixed_seller'] = fixed_seller
        except ObjectDoesNotExist:
            pass
    return dict

