from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    username = models.CharField(_('User name'), max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse_lazy('users:index')

    def __str__(self):
        return self.username
