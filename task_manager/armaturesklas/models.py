from django.db import models
from django.urls import reverse_lazy


class ArmatureKlas(models.Model):
    klas = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse_lazy('armaturesklas:index')

    def __str__(self):
        return f"{self.klas}"
