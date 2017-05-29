from user.models import AbstractUser, Student, Seller, WalkingSeller, FixedSeller
from django.core.exceptions import ObjectDoesNotExist


def user_processor(request):
    auth = False
    user = None
    auser = None
    seller = None
    student = None
    walking_seller = None
    fixed_seller = None

    if request.user.is_authenticated():
        user = request.user
        try:
            auser = AbstractUser.objects.get(user=user)
            auth = True
        except ObjectDoesNotExist:
            pass

        try:
            seller = Seller.objects.get(user=auser)
        except ObjectDoesNotExist:
            pass

        try:
            student = Student.objects.get(user=auser)
        except ObjectDoesNotExist:
            pass

        try:
            walking_seller = WalkingSeller.objects.get(super_seller=seller)
        except ObjectDoesNotExist:
            pass

        try:
            fixed_seller = FixedSeller.objects.get(super_seller=seller)
        except ObjectDoesNotExist:
            pass
    return {'logged_user': user,
            'logged_abstract_user': auser,
            'logged_seller': seller,
            'logged_student': student,
            'logged_walking_seller': walking_seller,
            'logged_fixed_seller': fixed_seller,
            'logged_auth': auth}

