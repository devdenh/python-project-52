from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from task_manager.projects.forms import ProjectsForm
from task_manager.projects.models import Projects


REGISTRATION_SUCCESS_MESSAGE = "Project created Successfully"
UPDATE_SUCCESS_MESSAGE = "Project updated Successfully"
DELETE_SUCCESS_MESSAGE = "Project deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Project are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Projects
    template_name = 'projects/index.html'


class ProjectsRegistrate(LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):

    form_class = ProjectsForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('projects:index')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class ProjectsUpdate(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UpdateView):

    model = Projects
    form_class = ProjectsForm
    template_name = 'projects/update.html'
    success_url = reverse_lazy('projects:index')
    success_message = UPDATE_SUCCESS_MESSAGE


class ProjectsDelete(LoginRequiredMixin,
                  SuccessMessageMixin,
                  DeleteView):

    model = Projects
    template_name = 'projects/delete.html'
    success_url = reverse_lazy('projects:index')
    success_message = DELETE_SUCCESS_MESSAGE
