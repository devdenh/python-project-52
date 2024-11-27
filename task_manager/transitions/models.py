from django.db import models
from django.urls import reverse_lazy

from task_manager.armatures.models import Armature
from task_manager.armaturesklas.models import ArmatureKlas
from task_manager.projects.models import Project


class Transition(models.Model):
    name = models.CharField(max_length=100) # Наименование
    volume = models.FloatField() # Объем
    thickness = models.CharField(max_length=100) # Толщина
    project_sheet = models.CharField(max_length=100) # Лист проекта
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # Проект

    def get_absolute_url(self):
        return reverse_lazy('transitions:index')

    def __str__(self):
        return self.name


class TransitionArmature(models.Model):
    ARMATURE_TYPE_CHOICES = [
        ('bent', 'Гнутый'),
        ('straight', 'Прямой'),
        ('stock', 'Погонаж'),
        ('frame', 'Для каркасов'),
    ]

    MANUFACTURE_PLACE_CHOICES = [
        ('factory', 'Завод'),
        ('site', 'Стройплощадка'),
    ]

    diameter = models.ForeignKey(Armature, on_delete=models.CASCADE)  # Диаметр, mm
    klas = models.ForeignKey(ArmatureKlas, on_delete=models.CASCADE)  # Класс
    bar_length = models.FloatField()  # Длина стержней
    bar_count = models.IntegerField()  # Кол-во стержней
    bar_type = models.CharField(max_length=20, choices=ARMATURE_TYPE_CHOICES)  # Вид стержня
    manufacture_place = models.CharField(max_length=20, choices=MANUFACTURE_PLACE_CHOICES)  # Место изготовления
    transition = models.ForeignKey(Transition, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Armature {self.diameter}mm, {self.klas}"
