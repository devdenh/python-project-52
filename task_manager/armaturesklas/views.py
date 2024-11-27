from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from task_manager.armaturesklas.forms import ArmatureKlasForm
from task_manager.armaturesklas.models import ArmatureKlas


REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = ArmatureKlas
    template_name = 'armaturesklas/index.html'


class ArmatureKlasRegistrate(LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):

    form_class = ArmatureKlasForm
    template_name = 'armaturesklas/create.html'
    success_url = reverse_lazy('armaturesklas:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class ArmatureKlasUpdate(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UpdateView):

    model = ArmatureKlas
    form_class = ArmatureKlasForm
    template_name = 'armaturesklas/update.html'
    success_url = reverse_lazy('armaturesklas:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class ArmatureKlasDelete(LoginRequiredMixin,
                  SuccessMessageMixin,
                  DeleteView):

    model = ArmatureKlas
    template_name = 'armaturesklas/delete.html'
    success_url = reverse_lazy('armaturesklas:index')
    success_message = DELETE_SUCCESS_MESSAGE
