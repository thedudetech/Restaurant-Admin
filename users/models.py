from django.db import models
import datetime

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=12)
    dob = models.DateField()
    photo = models.ImageField(upload_to='image', height_field=120, width_field=100, max_length=100)
    password = models.CharField(max_length=20)

def __str__(self):
    return '%s %s %s %s %s %s' % (self.user_name, self.email, self.mobile, self.dob,self.photo, self.password)