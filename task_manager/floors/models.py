from django.db import models
from django.urls import reverse_lazy

from task_manager.sections.models import Section


class Floor(models.Model):
    number = models.IntegerField() # Номер этажа
    tier_number = models.IntegerField() # Номер яруса
    floor_height = models.FloatField() # Высота вертикальных конструкций
    wall_height = models.FloatField() # Высота стен
    slab_thickness = models.FloatField() # Толщина перекрытий

    def get_absolute_url(self):
        return reverse_lazy('floors:index')

    def __str__(self):
        return str(self.number)


class SectionFloor(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)  # Связь с секцией
    floor_number = models.IntegerField()                            # Номер этажа
    tier_number = models.IntegerField()                             # Номер яруса
    floor_height = models.FloatField()                              # Высота этажа
    wall_column_height = models.FloatField()                        # Высота стен/колонн
    slab_thickness = models.FloatField()                            # Толщина перекрытия

    def __str__(self):
        return f"Floor {self.floor_number} of {self.section.name}"