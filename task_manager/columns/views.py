from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from task_manager.columns.forms import ColumnForm
from task_manager.columns.models import Column

REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Column
    template_name = 'columns/index.html'


class ColumnRegistrate(LoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):

    form_class = ColumnForm
    template_name = 'columns/create.html'
    success_url = reverse_lazy('columns:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class ColumnUpdate(LoginRequiredMixin,
                   SuccessMessageMixin,
                   UpdateView):

    model = Column
    form_class = ColumnForm
    template_name = 'columns/update.html'
    success_url = reverse_lazy('columns:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class ColumnDelete(LoginRequiredMixin,
                   SuccessMessageMixin,
                   DeleteView):

    model = Column
    template_name = 'columns/delete.html'
    success_url = reverse_lazy('columns:index')
    success_message = DELETE_SUCCESS_MESSAGE
