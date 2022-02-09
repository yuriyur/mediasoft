from django.test import TestCase
from shop.models import Shop
from city.models import City, Street
from shop.views import ShopFilter
import datetime
# Create your tests here.

class Shops(TestCase):

    def setUp(self):
        city = City.objects.create(name="Самара")
        street = Street.objects.create(name="Ленина", city_id=city)
        current = datetime.datetime.now().time()
        current = current.strftime("%H:%M")
        Shop.objects.create(name="Комод0", city=city, street=street, house=1, time_open=current, time_close=current)
        Shop.objects.create(name="Комод1", city=city, street=street, house=1, time_open=current, time_close=current)
        Shop.objects.create(name="Комод2", city=city, street=street, house=1, time_open=current, time_close=current)
        Shop.objects.create(name="Комод3", city=city, street=street, house=1, time_open=current, time_close=current)
        Shop.objects.create(name="Комод4", city=city, street=street, house=1, time_open=current, time_close=current)
        Shop.objects.create(name="Комод5", city=city, street=street, house=1, time_open=current, time_close=current)

    def test_correct_time_open_shops(self):
        queryset = Shop.objects.all()
        openvalue = ('1')
        closevalue = ('0')
        shops_open = list(ShopFilter.open__in(self, queryset, 0, openvalue))
        shops_close = list(ShopFilter.open__in(self, queryset, 0, closevalue))
        assert shops_open == shops_close
