from django.db import models
from django.urls import reverse_lazy


class Armature(models.Model):
    linear_weight = models.FloatField()
    diameter = models.FloatField()

    def get_absolute_url(self):
        return reverse_lazy('armatures:index')

    def __str__(self):
        return f"{self.diameter}"
