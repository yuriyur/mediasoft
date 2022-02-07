from django.urls import path
from city.views import CityListView, StreetListView, CityCreateView, StreetCreateView, StreetFilterView

app_name = 'city'
urlpatterns = [
    path('', CityListView.as_view()),
    path('street/', StreetListView.as_view()),
    path('create/', CityCreateView.as_view()),
    path('street/create/', StreetCreateView.as_view()),
    path('<int:city_id>/street/', StreetFilterView.as_view()),    
]