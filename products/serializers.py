from rest_framework import serializers
from .models import Products , Product_Category

class ProductsSerializers(serializers.ModelSerializer):
    

    class Meta:
        model = Products

        fields = "__all__"

class ProductsCatSerializers(serializers.ModelSerializer):
    

    class Meta:
        model = Product_Category ,

        fields = "__all__"