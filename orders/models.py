from django.db import models

# Create your models here.
class GetOrder(models.Model):
    kotid = models.CharField(max_length=30)
    item_name = models.CharField(max_length=30)
    note = models.CharField(max_length=30)
    qnty = models.CharField(max_length=3)
    price = models.CharField(max_length=6)