from tastypie.resources import ModelResource
from . import models 
from tastypie.authorization import Authorization
        

class UserResource(ModelResource):
    class Meta:
        queryset = models.Users.objects.all()
        resource_name = 'user'
        authorization = Authorization()