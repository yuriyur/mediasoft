from rest_framework import serializers
from shop.models import Shop


class ShopDetailSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Shop
        fields = '__all__'

class ShopTimeSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Shop
        fields = ('time_open', 'time_close', )

class ShopFilterSerializers(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    street = serializers.StringRelatedField()

    class Meta: 
        model = Shop
        fields = ('name', 'city', 'street', 'time_open', 'time_close')
