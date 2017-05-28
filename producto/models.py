from django.db import models
from user.models import Seller

# Create your models here.

class Producto(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    owner = models.ForeignKey(Seller)
