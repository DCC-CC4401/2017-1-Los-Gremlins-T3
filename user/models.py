from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Cada modelo se mapea a la base de datos de django


# Acount types:
# 0: null
# 1: Stundent
# 2: Walking Seller
# 3: Fixed Seller
# 4: Admin
class AbstractUser(models.Model):
    # Common data
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="abstract_user")
    fullname = models.TextField()
    photo = models.ImageField()
    account_type = models.IntegerField(default=0)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name):
        pay_method = cls(name=name)
        pay_method.save()
        return pay_method


class Seller(models.Model):
    # For user to make it fav and gather common data
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE, related_name='seller')
    payment_methods = models.ManyToManyField(PaymentMethod)
    times_favorited = models.IntegerField(default=0)


class Student(models.Model):
    # To extend the AbstractUser model we need to create a OneToOne realtionship
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE, related_name='student')
    favorites = models.ManyToManyField(Seller)

    def __str__(self):
        return self.user.fullname


class FixedSeller(models.Model):
    super_seller = models.OneToOneField(Seller, on_delete=models.CASCADE, related_name='fixed_seller')
    start_hour = models.TimeField(auto_now=True)
    end_hour = models.TimeField(auto_now=True)
    address = models.TextField(max_length=128)

    def __str__(self):
        return self.user.fullname


class WalkingSeller(models.Model):
    super_seller = models.OneToOneField(Seller, on_delete=models.CASCADE, related_name='walking_seller')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.fullname



