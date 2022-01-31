from cgitb import lookup
from rest_framework import serializers
from shop.models import Shop
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class ShopListSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Shop
        depth = 1
        fields = ('name', 'city', 'street')

class ShopDetailSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Shop
        fields = '__all__'

class ShopFilterSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Shop
        fields = ('name',)
