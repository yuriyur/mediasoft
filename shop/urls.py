from django.urls import path, include
from shop.views import CreateShopView

app_name = 'shop'
urlpatterns = [
    path('create/', CreateShopView.as_view()),
]