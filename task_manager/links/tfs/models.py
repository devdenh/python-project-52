from django.db import models
from django.urls import reverse_lazy

from task_manager.concrete.models import Concrete
from task_manager.floors.models import Floor
from task_manager.models import ArmatureMassCalculationMixin
from task_manager.sections.models import Section
from task_manager.transitions.models import Transition, TransitionArmature


class TFS(models.Model, ArmatureMassCalculationMixin):
    transition = models.ForeignKey(Transition, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    concrete = models.ForeignKey(Concrete, on_delete=models.CASCADE)
    axes = models.CharField(max_length=100)

    class Meta:
        unique_together = ['transition', 'floor', 'section', 'concrete', 'axes']

    def get_absolute_url(self):
        return reverse_lazy('tfs:index')

    def calculate_armature_mass(self):
        return super().calculate_armature_mass(TransitionArmature, 'transition')

    def __str__(self):
        return (f"Лестничная площадка {self.transition} "
                f"на этаже {self.floor} "
                f"в секции {self.section}")
