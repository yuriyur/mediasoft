from django.urls import path, include
from shop.views import ShopCreateView, ShopListView, ShopDetailView

app_name = 'shop'
urlpatterns = [
    path('', ShopCreateView.as_view()),
    path('all/', ShopListView.as_view()),
    path('edit/<int:pk>/', ShopDetailView.as_view()),
]