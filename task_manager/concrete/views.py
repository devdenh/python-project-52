from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from task_manager.concrete.forms import ConcreteForm
from task_manager.concrete.models import Concrete


REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Concrete
    template_name = 'concrete/index.html'


class ConcreteRegistrate(LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):

    form_class = ConcreteForm
    template_name = 'concrete/create.html'
    success_url = reverse_lazy('concrete:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class ConcreteUpdate(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UpdateView):

    model = Concrete
    form_class = ConcreteForm
    template_name = 'concrete/update.html'
    success_url = reverse_lazy('concrete:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class ConcreteDelete(LoginRequiredMixin,
                  SuccessMessageMixin,
                  DeleteView):

    model = Concrete
    template_name = 'concrete/delete.html'
    success_url = reverse_lazy('concrete:index')
    success_message = DELETE_SUCCESS_MESSAGE
