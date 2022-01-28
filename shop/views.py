from rest_framework import generics
from shop.serializers import ShopDetailSerializers, ShopListSerializers
from shop.models import Shop
# Create your views here.

class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopDetailSerializers

class ShopListView(generics.ListAPIView):
    serializer_class = ShopListSerializers
    queryset = Shop.objects.all()

class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopDetailSerializers
    queryset = Shop.objects.all()
