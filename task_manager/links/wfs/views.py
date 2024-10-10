from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DeleteView
from django.views.generic import (
    ListView, CreateView, UpdateView
)

from task_manager.links.wfs.forms import WFSForm
from task_manager.links.wfs.models import WFS

REGISTRATION_SUCCESS_MESSAGE = _("Label created Successfully")
UPDATE_SUCCESS_MESSAGE = _("Label updated Successfully")
DELETE_SUCCESS_MESSAGE = _("Label deleted Successfully")
LABEL_USED_MESSAGE = _("You can't delete labels are still being used")


class WFSView(LoginRequiredMixin,
                ListView):
    model = WFS
    template_name = 'links/wfs/index.html'


class WFSRegistrate(LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):

    form_class = WFSForm
    template_name = 'links/wfs/create.html'
    success_url = reverse_lazy('links:wfs:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class WFSUpdate(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UpdateView):

    model = WFS
    form_class = WFSForm
    template_name = 'links/wfs/update.html'
    success_url = reverse_lazy('links:wfs:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class WFSDelete(LoginRequiredMixin,
                  SuccessMessageMixin,
                  DeleteView):

    model = WFS
    template_name = 'links/wfs/delete.html'
    success_url = reverse_lazy('links:wfs:index')
    success_message = DELETE_SUCCESS_MESSAGE
