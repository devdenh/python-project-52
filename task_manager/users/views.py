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
from django.shortcuts import redirect


CREATION_SUCCESS_MESSAGE = _("Successful sign in")
CREATION_DENIED_MESSAGE = _("You are not authorized! Please, log in")


class IndexView(ListView):
    model = get_user_model()
    template_name = 'users/index.html'


class UserCreate(CreateView, SuccessMessageMixin):
    form_class = RegisterUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('root')
    success_message = CREATION_SUCCESS_MESSAGE


class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/update.html'
    permission_denied_message = CREATION_DENIED_MESSAGE
    success_url = reverse_lazy('users:index')

    def test_func(self):
        request = super().request
        if self.get_object().id == self.request.user.id:
            messages.error(request, CREATION_DENIED_MESSAGE)
        return redirect(reverse_lazy('login'))

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id == self.request.user.id:
            messages.error(request, CREATION_DENIED_MESSAGE)
        return super().dispatch(request, *args, **kwargs)


class UserDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:index')
    login_url = 'login'
    permission_denied_message = CREATION_DENIED_MESSAGE

    def test_func(self):
        return self.get_object().id == self.request.user.id
