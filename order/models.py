from django.db import models

from django.utils import timezone


class Order(models.Model):
    order_id = models.CharField(max_length=40, primary_key=True)
    manager_id = models.CharField(max_length=40)
    #manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    t_price = models.CharField(max_length=40)




# Create your models here.
