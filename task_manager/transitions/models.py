from django.db import models
from django.urls import reverse_lazy


class Transition(models.Model):
    name = models.CharField(max_length=100) # Наименование
    volume = models.FloatField() # Объем
    thickness = models.CharField(max_length=100) # Толщина

    def get_absolute_url(self):
        return reverse_lazy('transitions:index')

    def __str__(self):
        return self.name
