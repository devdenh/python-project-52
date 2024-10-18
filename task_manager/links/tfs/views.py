from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DeleteView
from django.views.generic import (
    ListView, CreateView, UpdateView
)

from task_manager.links.tfs.forms import TFSForm
from task_manager.links.tfs.models import TFS

REGISTRATION_SUCCESS_MESSAGE = _("Label created Successfully")
UPDATE_SUCCESS_MESSAGE = _("Label updated Successfully")
DELETE_SUCCESS_MESSAGE = _("Label deleted Successfully")
LABEL_USED_MESSAGE = _("You can't delete labels are still being used")


class TFSView(LoginRequiredMixin,
                ListView):
    model = TFS
    template_name = 'links/tfs/index.html'


class TFSRegistrate(LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):

    form_class = TFSForm
    template_name = 'links/tfs/create.html'
    success_url = reverse_lazy('links:tfs:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class TFSUpdate(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UpdateView):

    model = TFS
    form_class = TFSForm
    template_name = 'links/tfs/update.html'
    success_url = reverse_lazy('links:tfs:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class TFSDelete(LoginRequiredMixin,
                  SuccessMessageMixin,
                  DeleteView):

    model = TFS
    template_name = 'links/tfs/delete.html'
    success_url = reverse_lazy('links:tfs:index')
    success_message = DELETE_SUCCESS_MESSAGE
