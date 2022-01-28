from django.db import models
from city.models import City, Street
# Create your models here.

class Shop(models.Model):
    name = models.CharField(verbose_name='Магазин', max_length=64)
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE)
    street = models.ForeignKey(Street, verbose_name='Улица', on_delete=models.CASCADE)
    house = models.PositiveIntegerField(verbose_name='Номер дома')
    time_open = models.TimeField(verbose_name='Время открытия')
    time_close = models.TimeField(verbose_name='Время закрытия')
