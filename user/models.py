from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Alumno(models.Model):
    # To extend the Django User model we need to create a OneToOne realtionship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The user can rate strains so it has a review_set

    def __str__(self):
        return self.user.username

class VendedorAmbulante(models.Model):
    # To extend the Django User model we need to create a OneToOne realtionship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The user can rate strains so it has a review_set

    def __str__(self):
        return self.user.username

class VendedorFijo(models.Model):
    # To extend the Django User model we need to create a OneToOne realtionship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The user can rate strains so it has a review_set

    def __str__(self):
        return self.user.username