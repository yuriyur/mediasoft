from django.urls import path, include
from city.views import CityListView, StreetListView, CityCreateView, StreetCreateView

app_name = 'city'
urlpatterns = [
    path('', CityListView.as_view()),
    path('street/', StreetListView.as_view()),
    path('create/', CityCreateView.as_view()),
    path('street/create/', StreetCreateView.as_view()),
]