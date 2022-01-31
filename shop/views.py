from rest_framework import generics
from shop.serializers import ShopDetailSerializers, ShopListSerializers, ShopFilterSerializers
from shop.models import Shop
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django_filters import TimeRangeFilter,TimeFilter
import datetime
# Create your views here.

class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopDetailSerializers

class ShopListView(generics.ListAPIView):
    serializer_class = ShopListSerializers
    queryset = Shop.objects.all()

class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopDetailSerializers
    queryset = Shop.objects.all()

class ShopFilter(filters.FilterSet):
    class Meta:
        model = Shop
        fields = ['street', 'city']

class ShopFilterView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopFilterSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ShopFilter
