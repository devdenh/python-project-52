from django.db import models
from django.urls import reverse_lazy


class Column(models.Model):
    name = models.CharField(max_length=100) # Наименование колонны
    length = models.FloatField() # Длина в сечении
    width = models.FloatField() # Ширина в сечении

    def get_absolute_url(self):
        return reverse_lazy('sections:index')

    def __str__(self):
        return self.name
