from django.views.generic import (
    ListView, CreateView, UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from task_manager.labels.forms import LabelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect


REGISTRATION_SUCCESS_MESSAGE = _("Label created Successfully")
UPDATE_SUCCESS_MESSAGE = _("Label updated Successfully")
DELETE_SUCCESS_MESSAGE = _("Label deleted Successfully")
STATUS_USED_MESSAGE = _("You can't delete labels are still being used")


class IndexView(LoginRequiredMixin,
                ListView):
    model = Label
    template_name = 'labels/index.html'


class LabelRegistrate(LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):

    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class LabelUpdate(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UpdateView):

    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class LabelDelete(LoginRequiredMixin,
                  SuccessMessageMixin,
                  DeleteView):

    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:index')
    success_message = DELETE_SUCCESS_MESSAGE

    def form_valid(self, form):
        if Task.objects.filter(label=self.kwargs['pk']):
            messages.error(self.request, STATUS_USED_MESSAGE)
            return redirect(reverse_lazy('labels:index'))
        return super().form_valid(form)
