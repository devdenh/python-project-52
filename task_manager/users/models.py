from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    username = models.CharField(_('User name'), max_length=100, unique=True)
    # password = models.CharField(_('Password'), max_length=100, unique=True, default='')
    # last_login = models.DateTimeField(auto_now_add=True)
    # is_superuser = False
    # username = models.CharField(_('User name'), max_length=100, unique=True)
    # email = models.CharField(_('Email'), max_length=100, default='')
    # is_staff = False
    # is_active = ''
    # date_joined = models.DateTimeField(auto_now_add=True)

    # first_name = models.CharField(_('First_name'), max_length=100, default=_(''))
    # last_name = models.CharField(_('Last_name'), max_length=100, default='')
    # created_at = models.DateTimeField(_('Created at'), default=timezone.now)
    # USERNAME_FIELD = _('username')

    def get_absolute_url(self):
        return reverse_lazy('users:index')

    def __str__(self):
        return self.username
