from django.db import models
from django.urls import reverse_lazy


class Slab(models.Model):
    name = models.CharField(max_length=100) # Наименование перекрытия
    volume = models.FloatField() # объем
    thickness = models.FloatField() # толщина

    def get_absolute_url(self):
        return reverse_lazy('slabs:index')

    def __str__(self):
        return self.name
