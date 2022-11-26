from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext as _
from django.contrib import messages
from task_manager.forms import UserLoginForm


SUCCESS_LOGGED_IN_MESSAGE = _("You are logged in")
LOGGED_OUT_MESSAGE = _("You are logged out")


class IndexView(TemplateView):
    template_name = 'index.html'

    def index(request):
        a = None
        a.hello()  # Creating an error with an invalid line of code
        return HttpResponse("Hello, world. You're at the pollapp index.")


class UserLogin(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = 'root'
    success_message = SUCCESS_LOGGED_IN_MESSAGE


class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, LOGGED_OUT_MESSAGE)
        return super().dispatch(request, *args, **kwargs)
