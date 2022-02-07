from rest_framework import generics
from city.serializers import CityDetailSerializers, StreetDetailSerializers
from city.models import City, Street
from django_filters import rest_framework as filters
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

class StreetFilterView(generics.ListAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetDetailSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('city_id', )

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(city_id=self.kwargs.get('city_id'))