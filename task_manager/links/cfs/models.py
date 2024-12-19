from django.db import models
from django.urls import reverse_lazy

from task_manager.columns.models import Column, ColumnArmature
from task_manager.concrete.models import Concrete
from task_manager.floors.models import Floor
from task_manager.models import ArmatureMassCalculationMixin
from task_manager.sections.models import Section


class CFS(models.Model, ArmatureMassCalculationMixin):
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    concrete = models.ForeignKey(Concrete, on_delete=models.CASCADE)
    axes = models.CharField(max_length=100)

    class Meta:
        unique_together = ['column', 'floor', 'section', 'concrete', 'axes']

    def get_absolute_url(self):
        return reverse_lazy('cfs:index')

    def calculate_armature_mass(self):
        return super().calculate_armature_mass(ColumnArmature, 'column')

    def __str__(self):
        return (f"Колонна {self.column} "
                f"на этаже {self.floor} "
                f"в секции {self.section}")
