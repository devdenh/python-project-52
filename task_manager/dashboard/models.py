from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from task_manager.columns.models import Column
from task_manager.concrete.models import Concrete
from task_manager.floors.models import Floor
from task_manager.links.cfs.models import CFS
from task_manager.links.sfs.models import SFS
from task_manager.links.tfs.models import TFS
from task_manager.links.wfs.models import WFS
from task_manager.projects.models import Project
from task_manager.sections.models import Section
from task_manager.slabs.models import Slab
from task_manager.transitions.models import Transition
from task_manager.users.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Statuses
from django.utils import timezone

from task_manager.walls.models import Wall


class Dashboard(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    column = models.ForeignKey(Column, null=True, blank=True, on_delete=models.SET_NULL)
    wall = models.ForeignKey(Wall, null=True, blank=True, on_delete=models.SET_NULL)
    slab = models.ForeignKey(Slab, null=True, blank=True, on_delete=models.SET_NULL)
    transition = models.ForeignKey(Transition, null=True, blank=True, on_delete=models.SET_NULL)
    concrete = models.ForeignKey(Concrete, null=True, blank=True, on_delete=models.SET_NULL)

    # Связи для различных конструкций
    cfs = models.ForeignKey(CFS, null=True, blank=True, on_delete=models.SET_NULL)
    sfs = models.ForeignKey(SFS, null=True, blank=True, on_delete=models.SET_NULL)
    tfs = models.ForeignKey(TFS, null=True, blank=True, on_delete=models.SET_NULL)
    wfs = models.ForeignKey(WFS, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Dashboard for {self.project} - {self.section} - Floor {self.floor.number}"
