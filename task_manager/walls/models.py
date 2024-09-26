from django.db import models
from django.urls import reverse_lazy

from task_manager.sections.models import SectionFloor


class Wall(models.Model):
    name = models.CharField(max_length=100) # Наименование стены
    volume = models.FloatField() # Объем
    thickness = models.CharField(max_length=100) # Толщина
    section_floor = models.ForeignKey(SectionFloor, on_delete=models.CASCADE)  # Связь с этажом секции

    def get_absolute_url(self):
        return reverse_lazy('sections:index')

    def __str__(self):
        return self.name
