from tkinter import CASCADE
from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(verbose_name='Город', max_length=64)

class Street(models.Model):
    name = models.CharField(verbose_name='Улица', max_length=64)
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE)
