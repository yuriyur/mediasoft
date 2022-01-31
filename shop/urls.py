from django.urls import path
from shop.views import ShopCreateView, ShopListView, ShopDetailView, ShopFilterView

app_name = 'shop'
urlpatterns = [
    path('create/', ShopCreateView.as_view()),
    path('all/', ShopListView.as_view()),
    path('edit/<int:pk>/', ShopDetailView.as_view()),
    path('', ShopFilterView.as_view()),
]