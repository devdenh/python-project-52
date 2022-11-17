from django.views.generic import (
    ListView, CreateView, UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from task_manager.statuses.models import Statuses
from task_manager.statuses.forms import StatusesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy


REGISTRATION_SUCCESS_MESSAGE = _("Status created Successfully")
UPDATE_SUCCESS_MESSAGE = _("Status updated Successfully")
DELETE_SUCCESS_MESSAGE = _("Status deleted Successfully")


class IndexView(LoginRequiredMixin,
                ListView):
    model = Statuses
    template_name = 'statuses/index.html'


class StatusRegistrate(LoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):

    form_class = StatusesForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class StatusUpdate(LoginRequiredMixin,
                   SuccessMessageMixin,
                   UpdateView):

    model = Statuses
    form_class = StatusesForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class StatusDelete(LoginRequiredMixin,
                   SuccessMessageMixin,
                   DeleteView):

    model = Statuses
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses:index')
    success_message = DELETE_SUCCESS_MESSAGE
