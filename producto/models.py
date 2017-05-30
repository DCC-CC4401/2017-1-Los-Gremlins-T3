from django.db import models
from user.models import Seller

# Create your models here.

class Producto(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.TextField(max_length=128)
    description = models.TextField()
    owner = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    photo = models.ImageField()
    prev_img_id = models.IntegerField()

