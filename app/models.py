from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=32, unique=True)


class Product(models.Model):
    title = models.CharField(max_length=64)
    sku = models.CharField(max_length=32, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product_brand')


class Size(models.Model):
    title = models.CharField(max_length=16)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='size')


class Price(models.Model):
    price = models.IntegerField(default=0)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='price_size')
    date_updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.price}, {self.size}, {self.date_updated}"
