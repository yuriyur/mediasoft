from django.urls import path, include
from city.views import CityListView, StreetListView

app_name = 'city'
urlpatterns = [
    path('', CityListView.as_view()),
    path('street/', StreetListView.as_view()),
]