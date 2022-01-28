from django.shortcuts import render
from rest_framework import generics
from shop.serializers import ShopDetailSerializers
# Create your views here.

class CreateShopView(generics.CreateAPIView):
    serializer_class = ShopDetailSerializers