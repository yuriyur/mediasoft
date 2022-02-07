from rest_framework import serializers
from city.models import City, Street

class CityDetailSerializers(serializers.ModelSerializer):
    class Meta: 
        model = City
        fields = '__all__'

class StreetDetailSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Street
        fields = '__all__'

class CityShopSerializers(serializers.ModelSerializer):
    class Meta: 
        model = City
        fields = ('name', )

class StreetShopSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Street
        fields = ('name', )