from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from task_manager.armatures.forms import ArmatureForm
from task_manager.armatures.models import Armature


REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Armature
    template_name = 'armatures/index.html'


class ArmatureRegistrate(LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):

    form_class = ArmatureForm
    template_name = 'armatures/create.html'
    success_url = reverse_lazy('armatures:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class ArmatureUpdate(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UpdateView):

    model = Armature
    form_class = ArmatureForm
    template_name = 'armatures/update.html'
    success_url = reverse_lazy('armatures:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class ArmatureDelete(LoginRequiredMixin,
                  SuccessMessageMixin,
                  DeleteView):

    model = Armature
    template_name = 'armatures/delete.html'
    success_url = reverse_lazy('armatures:index')
    success_message = DELETE_SUCCESS_MESSAGE
