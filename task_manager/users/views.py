from django.views.generic import (
    ListView, CreateView, UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from task_manager.users.models import User
from task_manager.users.forms import UserForm, RegisterUserForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib import messages


REGISTRATION_SUCCESS_MESSAGE = _("Successful sign up")
UPDATE_USER_SUCCESS_MESSAGE = _("User successfully changed")
AUTH_DENIED_MESSAGE = _("You are not authorized! Please, log in")
DELETE_SUCCESS_MESSAGE = _("User successfully deleted")


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
    form_class = UserForm
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
                 UserPassesTestMixin,
                 SuccessMessageMixin,
                 DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:index')
    login_url = 'login'
    success_message = DELETE_SUCCESS_MESSAGE

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id != self.request.user.id:
            messages.error(request, AUTH_DENIED_MESSAGE)
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.get_object().id == self.request.user.id
