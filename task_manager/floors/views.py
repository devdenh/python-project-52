from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from task_manager.floors.forms import FloorForm
from task_manager.floors.models import Floor

REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Floor
    template_name = 'floors/index.html'


class FloorRegistrate(LoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):

    form_class = FloorForm
    template_name = 'floors/create.html'
    success_url = reverse_lazy('floors:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class FloorUpdate(LoginRequiredMixin,
                   SuccessMessageMixin,
                   UpdateView):

    model = Floor
    form_class = FloorForm
    template_name = 'floors/update.html'
    success_url = reverse_lazy('floors:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class FloorDelete(LoginRequiredMixin,
                   SuccessMessageMixin,
                   DeleteView):

    model = Floor
    template_name = 'floors/delete.html'
    success_url = reverse_lazy('floors:index')
    success_message = DELETE_SUCCESS_MESSAGE
