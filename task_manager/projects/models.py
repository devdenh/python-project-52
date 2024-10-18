from django.db import models
from django.urls import reverse_lazy


class Project(models.Model):
    designation = models.CharField(max_length=100)  # Шифр проекта
    name = models.CharField(max_length=255)         # Наименование
    change_number = models.FloatField()             # Номер изменений
    issue_date = models.DateField()                 # Дата выдачи

    def get_absolute_url(self):
        return reverse_lazy('projects:index')

    def __str__(self):
        return self.designation
