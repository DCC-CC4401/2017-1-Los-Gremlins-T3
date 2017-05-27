from django.conf import settings
from django.db import models


# Cada modelo se mapea a la base de datos de django
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    fullname = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname',]

    def get_full_name(self):
        return self.fullname

    def get_short_name(self):
        return self.get_full_name()


class Alumno(models.Model):
    # To extend the Django User model we need to create a OneToOne realtionship
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField(max_length=128)

    def __str__(self):
        return self.user.first_name + self.user.last_name


class VendedorAbstracto(models.Model):
    # Superclass, shouldn't be instantiated
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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

