from django.db import models
import datetime
from multiselectfield import MultiSelectField
# from select_multiple_field import SelectMultipleField
# from select_multiple_field.codecs import *
# Create your models here.
class Products(models.Model):
    

    ADDITIONALS = ((1, 'Item title 2.1'),
               (2, 'Item title 2.2'),
               (3, 'Item title 2.3'),
               (4, 'Item title 2.4'),
               (5, 'Item title 2.5'))
    product_photo = models.ImageField(upload_to='image', height_field=120, width_field=100, max_length=100)
    # product_type = models.CharField(max_length=30, choices=PRODUCT_TYPE)
    food_region = models.CharField(max_length=30)
    product_name = models.CharField(max_length=30)
    product_details = models.CharField(max_length=250)
    additionals = MultiSelectField(choices=ADDITIONALS,
                                 max_choices=10,
                                 max_length=30)
    product_quantity = models.CharField(max_length=12)
    product_price = models.CharField(max_length=12)
    
class Product_Category(models.Model):
    food_region = models.CharField(max_length=30)

class Product_Additionals(models.Model):
    ad_product = models.CharField(max_length=30)
    ad_price = models.CharField(max_length=30)