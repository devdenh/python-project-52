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


class SectionFloor(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)  # Связь с секцией
    floor_number = models.IntegerField()                            # Номер этажа
    tier_number = models.IntegerField()                             # Номер яруса
    floor_height = models.FloatField()                              # Высота этажа
    wall_column_height = models.FloatField()                        # Высота стен/колонн
    slab_thickness = models.FloatField()                            # Толщина перекрытия

    def __str__(self):
        return f"Floor {self.floor_number} of {self.section.name}"