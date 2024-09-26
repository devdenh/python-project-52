from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from task_manager.slabs.forms import SlabForm
from task_manager.slabs.models import Slab

REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Slab
    template_name = 'slabs/index.html'


class SlabRegistrate(LoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):

    form_class = SlabForm
    template_name = 'slabs/create.html'
    success_url = reverse_lazy('slabs:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class SlabUpdate(LoginRequiredMixin,
                   SuccessMessageMixin,
                   UpdateView):

    model = Slab
    form_class = SlabForm
    template_name = 'slabs/update.html'
    success_url = reverse_lazy('slabs:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class SlabDelete(LoginRequiredMixin,
                   SuccessMessageMixin,
                   DeleteView):

    model = Slab
    template_name = 'slabs/delete.html'
    success_url = reverse_lazy('slabs:index')
    success_message = DELETE_SUCCESS_MESSAGE
