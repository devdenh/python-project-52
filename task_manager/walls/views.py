from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from task_manager.walls.forms import WallForm
from task_manager.walls.models import Wall

REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Wall
    template_name = 'walls/index.html'


class WallRegistrate(LoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):

    form_class = WallForm
    template_name = 'walls/create.html'
    success_url = reverse_lazy('walls:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class WallUpdate(LoginRequiredMixin,
                   SuccessMessageMixin,
                   UpdateView):

    model = Wall
    form_class = WallForm
    template_name = 'walls/update.html'
    success_url = reverse_lazy('walls:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class WallDelete(LoginRequiredMixin,
                   SuccessMessageMixin,
                   DeleteView):

    model = Wall
    template_name = 'walls/delete.html'
    success_url = reverse_lazy('walls:index')
    success_message = DELETE_SUCCESS_MESSAGE
