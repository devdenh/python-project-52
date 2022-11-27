from django.views.generic import (
    ListView, CreateView, UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from task_manager.users.models import User
from task_manager.users.forms import RegisterUserForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from task_manager.tasks.models import Task
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


REGISTRATION_SUCCESS_MESSAGE = _("Successful sign up")
UPDATE_USER_SUCCESS_MESSAGE = _("User successfully changed")
AUTH_DENIED_MESSAGE = _("You are not authorized! Please, log in")
DELETE_SUCCESS_MESSAGE = _("User successfully deleted")
BOUND_DENIED_MESSAGE = _("Cannot delete user because it is in use")
PERMISSION_DENIED_MESSAGE = _("You don't have permission to change another user.")


class IndexView(ListView):
    model = get_user_model()
    template_name = 'users/index.html'


class UserRegistrate(SuccessMessageMixin,
                     CreateView):
    form_class = RegisterUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = REGISTRATION_SUCCESS_MESSAGE


class UserUpdate(LoginRequiredMixin,
                 UserPassesTestMixin,
                 SuccessMessageMixin,
                 UpdateView):

    model = User
    form_class = RegisterUserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:index')
    success_message = UPDATE_USER_SUCCESS_MESSAGE

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id != self.request.user.id:
            messages.error(request, AUTH_DENIED_MESSAGE)
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.get_object().id == self.request.user.id


class UserDelete(LoginRequiredMixin,
                 SuccessMessageMixin,
                 DeleteView):

    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:index')
    success_message = DELETE_SUCCESS_MESSAGE

    def form_valid(self, form):
        if self.get_object().id != self.request.user.id:
            messages.error(self.request, PERMISSION_DENIED_MESSAGE)
            return redirect(reverse_lazy('users:index'))

        bounds = Task.objects.values_list("executor", "author")
        if list(filter(lambda pk: self.kwargs['pk'], bounds)):
            messages.error(self.request, BOUND_DENIED_MESSAGE)
            return redirect(reverse_lazy('users:index'))

        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, AUTH_DENIED_MESSAGE)
        return redirect(reverse_lazy('login'))
