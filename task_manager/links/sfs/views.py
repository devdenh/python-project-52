from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DeleteView
from django.views.generic import (
    ListView, CreateView, UpdateView
)

from task_manager.links.sfs.forms import SFSForm
from task_manager.links.sfs.models import SFS

REGISTRATION_SUCCESS_MESSAGE = _("Label created Successfully")
UPDATE_SUCCESS_MESSAGE = _("Label updated Successfully")
DELETE_SUCCESS_MESSAGE = _("Label deleted Successfully")
LABEL_USED_MESSAGE = _("You can't delete labels are still being used")


class SFSView(LoginRequiredMixin,
                ListView):
    model = SFS
    template_name = 'links/sfs/index.html'


class SFSRegistrate(LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):

    form_class = SFSForm
    template_name = 'links/sfs/create.html'
    success_url = reverse_lazy('links:sfs:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class SFSUpdate(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UpdateView):

    model = SFS
    form_class = SFSForm
    template_name = 'links/sfs/update.html'
    success_url = reverse_lazy('links:sfs:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class SFSDelete(LoginRequiredMixin,
                  SuccessMessageMixin,
                  DeleteView):

    model = SFS
    template_name = 'links/sfs/delete.html'
    success_url = reverse_lazy('links:sfs:index')
    success_message = DELETE_SUCCESS_MESSAGE
