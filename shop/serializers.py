from rest_framework import serializers
from shop.models import Shop

class ShopDetailSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Shop
        fields = '__all__'