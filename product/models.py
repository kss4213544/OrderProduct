from django.db import models

from django.utils import timezone


class Product(models.Model):
    product_id = models.CharField(max_length=40, primary_key=True)
    product_name = models.CharField(max_length=40)
    product_price = models.CharField(max_length=40)
    category = models.CharField(max_length=40)




