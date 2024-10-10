from django.db import models
from django.urls import reverse_lazy


class Section(models.Model):
    name = models.CharField(max_length=100)  # Наименование секции
    axes_location = models.CharField(max_length=255)  # Оси расположения
    bottom_floor_mark = models.FloatField()  # Относительная отметка
    absolute_zero_mark = models.FloatField()  # Абсолютная отметка

    def get_absolute_url(self):
        return reverse_lazy('sections:index')

    def __str__(self):
        return self.name
