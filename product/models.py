from django.db import models

from django.utils import timezone


class Product(models.Model):
    Product_id = models.CharField(max_length=40, primary_key=True)
    Product_name = models.CharField(max_length=40)
    Product_price = models.CharField(max_length=40)
    Category = models.CharField(max_length=40)




