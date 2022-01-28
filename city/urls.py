from django.contrib import admin
from django.urls import path, include
from city.views import *

app_name = 'city'
urlpatterns = [
    #path('api/v1/city/', include('city.urls')),
    #path('shop/create', ShopCreateView.as_view()),
]