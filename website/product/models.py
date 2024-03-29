from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, models.PROTECT, 'accesses')
    is_valid = models.BooleanField(default=True)
