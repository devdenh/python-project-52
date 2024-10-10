from django.db import models
from django.urls import reverse_lazy

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
