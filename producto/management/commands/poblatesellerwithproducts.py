from django.core.management import BaseCommand
from user.models import AbstractUser, User, Seller, WalkingSeller
from producto.models import Producto
from django.contrib.auth.models import User



class Command(BaseCommand):
    def handle(self, *args, **options):
        duser = User.objects.create_user('vendedor@vendedor.vendedor', 'vendedor@vendedor.vendeor', 'vendedor')
        auser = AbstractUser(user=duser, fullname="Vendedor Default", account_type=2)
        auser.save()
        seller = Seller(user=auser)
        seller.save()
        walking_seller = WalkingSeller(super_seller=seller)
        walking_seller.save()

        producto1 = Producto(name='arroz',
                             price='1000',
                             stock='100',
                             description='rico arroz',
                             owner=seller,
                             prev_img_id=1)
        producto1.save()
        producto2 = Producto(name='pollo',
                             price='2000',
                             stock='200',
                             description='rico pollo',
                             owner=seller,
                             prev_img_id=2)
        producto2.save()
        producto3 = Producto(name='mierda',
                             price='10',
                             stock='9999',
                             description='llevatela por favor',
                             owner=seller,
                             prev_img_id=3)
        producto3.save()

        print("done")


