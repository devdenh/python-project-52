from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DeleteView
from django.views.generic import (
    ListView, CreateView, UpdateView
)

from task_manager.links.cfs.forms import CFSForm
from task_manager.links.cfs.models import CFS

REGISTRATION_SUCCESS_MESSAGE = _("Label created Successfully")
UPDATE_SUCCESS_MESSAGE = _("Label updated Successfully")
DELETE_SUCCESS_MESSAGE = _("Label deleted Successfully")
LABEL_USED_MESSAGE = _("You can't delete labels are still being used")


class CFSView(LoginRequiredMixin,
                ListView):
    model = CFS
    template_name = 'links/cfs/index.html'


class CFSRegistrate(LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):

    form_class = CFSForm
    template_name = 'links/cfs/create.html'
    success_url = reverse_lazy('links:cfs:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class CFSUpdate(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UpdateView):

    model = CFS
    form_class = CFSForm
    template_name = 'links/cfs/update.html'
    success_url = reverse_lazy('links:cfs:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class CFSDelete(LoginRequiredMixin,
                  SuccessMessageMixin,
                  DeleteView):

    model = CFS
    template_name = 'links/cfs/delete.html'
    success_url = reverse_lazy('links:cfs:index')
    success_message = DELETE_SUCCESS_MESSAGE
