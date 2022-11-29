from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Statuses
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(_("Name"), unique=True, max_length=100)
    description = models.TextField(_("Description"))
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="author", null=True)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name="executor", null=True)
    created_at = models.DateTimeField(default=timezone.now)
    labels = models.ManyToManyField(Label)

    def get_absolute_url(self):
        return reverse_lazy('tasks:index')

    def __str__(self):
        return self.name
