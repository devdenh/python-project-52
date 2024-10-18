from django.db import models
from django.urls import reverse_lazy

from task_manager.projects.models import Project


class Column(models.Model):
    name = models.CharField(max_length=100) # Наименование колонны
    volume = models.FloatField() # Объем
    project_sheet = models.CharField(max_length=100) # Лист проекта
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # Проект

    def get_absolute_url(self):
        return reverse_lazy('columns:index')

    def __str__(self):
        return self.name
