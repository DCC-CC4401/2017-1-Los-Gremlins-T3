from django.db import models
from django.contrib.auth.models import User


# Cada modelo se mapea a la base de datos de django
class Alumno(models.Model):
    # To extend the Django User model we need to create a OneToOne realtionship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=128)

    def __str__(self):
        return self.user.first_name + self.user.last_name


class VendedorAbstracto(models.Model):
    # Superclass, shouldn't be instantiated
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payMethods = models.CommaSeparatedIntegerField(max_length=10)

    def __str__(self):
        return self.user.first_name + self.user.last_name


class VendedorFijo(models.Model):
    # Mantiene informacion en comun
    superSeller = models.OneToOneField(VendedorAbstracto, on_delete=models.CASCADE)
    start_hour = models.TimeField(auto_now=True)
    end_hour = models.TimeField(auto_now=True)
    adress = models.TextField(max_length=128)

    def __str__(self):
        return self.superSeller.user.first_name + self.superSeller.user.last_name



class VendedorAmbulante(models.Model):
    superSeller = models.OneToOneField(VendedorAbstracto, on_delete=models.CASCADE)

    def __str__(self):
        return self.superSeller.user.first_name + self.superSeller.user.last_name

