from rest_framework import generics
from city.serializers import CityDetailSerializers, StreetDetailSerializers
from city.models import City, Street

# Create your views here.

class CityCreateView(generics.CreateAPIView):
    serializer_class = CityDetailSerializers

class StreetCreateView(generics.CreateAPIView):
    serializer_class = StreetDetailSerializers

class CityListView(generics.ListAPIView):
    serializer_class = CityDetailSerializers
    queryset = City.objects.all()

class StreetListView(generics.ListAPIView):
    serializer_class = StreetDetailSerializers
    queryset = Street.objects.all()
