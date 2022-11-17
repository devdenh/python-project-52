from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.utils import timezone


class Statuses(models.Model):
    name = models.CharField(_('Name'), max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse_lazy('statuses:index')

    def __str__(self):
        return self.name
