from django.core.management import BaseCommand
from user.models import PaymentMethod

METHODS = ["Efectivo",
           "Tarjeta de credito",
           "Tarjeta de debito",
           "Tarjeta Junaeb",
           ]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for method in METHODS:
            PaymentMethod.create(name=method)
        print("done")



