from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from task_manager.sections.forms import SectionForm
from task_manager.sections.models import Section


REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Section
    template_name = 'sections/index.html'


class SectionRegistrate(LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):

    form_class = SectionForm
    template_name = 'sections/create.html'
    success_url = reverse_lazy('sections:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class SectionUpdate(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UpdateView):

    model = Section
    form_class = SectionForm
    template_name = 'sections/update.html'
    success_url = reverse_lazy('sections:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class SectionDelete(LoginRequiredMixin,
                  SuccessMessageMixin,
                  DeleteView):

    model = Section
    template_name = 'sections/delete.html'
    success_url = reverse_lazy('sections:index')
    success_message = DELETE_SUCCESS_MESSAGE
