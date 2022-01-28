from rest_framework import generics
from city.serializers import CityDetailSerializers, StreetDetailSerializers
from city.models import City, Street

# Create your views here.

class CityListView(generics.ListAPIView):
    serializer_class = CityDetailSerializers
    queryset = City.objects.all()

class StreetListView(generics.ListAPIView):
    serializer_class = StreetDetailSerializers
    queryset = Street.objects.all()
