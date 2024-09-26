from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from task_manager.transitions.forms import TransitionForm
from task_manager.transitions.models import Transition

REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Transition
    template_name = 'transitions/index.html'


class TransitionRegistrate(LoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):

    form_class = TransitionForm
    template_name = 'transitions/create.html'
    success_url = reverse_lazy('transitions:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class TransitionUpdate(LoginRequiredMixin,
                   SuccessMessageMixin,
                   UpdateView):

    model = Transition
    form_class = TransitionForm
    template_name = 'transitions/update.html'
    success_url = reverse_lazy('transitions:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class TransitionDelete(LoginRequiredMixin,
                   SuccessMessageMixin,
                   DeleteView):

    model = Transition
    template_name = 'transitions/delete.html'
    success_url = reverse_lazy('transitions:index')
    success_message = DELETE_SUCCESS_MESSAGE
