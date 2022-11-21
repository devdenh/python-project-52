from django.views.generic import (
    ListView, CreateView, UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from task_manager.statuses.models import Statuses
from task_manager.statuses.forms import StatusesForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from task_manager.tasks.models import Task
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect


REGISTRATION_SUCCESS_MESSAGE = _("Status created Successfully")
UPDATE_SUCCESS_MESSAGE = _("Status updated Successfully")
DELETE_SUCCESS_MESSAGE = _("Status deleted Successfully")
STATUS_USED_MESSAGE = _("You can't delete statuses are still being used by a task")


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

    def form_valid(self, form):
        if Task.objects.filter(status=self.kwargs['pk']):
            messages.error(self.request, STATUS_USED_MESSAGE)
            return redirect(reverse_lazy('statuses:index'))
        return super().form_valid(form)
