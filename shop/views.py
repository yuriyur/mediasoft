from rest_framework import generics
from shop.serializers import ShopDetailSerializers, ShopListSerializers, ShopFilterSerializers, ShopTimeSerializers
from shop.models import Shop
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
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
    open = filters.CharFilter(method='open__in')

    def open__in(self, queryset, value, *args, **kwargs):
        current = datetime.datetime.now().time()
        current = current.strftime("%H:%M")
        if (args[0] == '1'):
            queryset = queryset.filter(time_open__lte=current, time_close__gte=current)
        elif (args[0] == '0'):
            queryset = queryset.filter(time_open__gte=current, time_close__gte=current) | queryset.filter(time_open__lte=current, time_close__lte=current)
        else:
            pass
        return queryset

    class Meta:
        model = Shop
        fields = ['street', 'city', 'open']

class ShopFilterView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopFilterSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ShopFilter
